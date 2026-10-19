
import time
from typing import Iterable, Optional

from pinecone import Pinecone, ServerlessSpec
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

from app.core.config import get_settings


# Load application configuration
settings = get_settings()


# Cache initialized objects within this Python process
_embeddings: Optional[OpenAIEmbeddings] = None
_vectorstore: Optional[PineconeVectorStore] = None


# Known dimensions for supported OpenAI embedding models
EMBEDDING_DIMENSIONS = {
    "text-embedding-3-small": 1536,
    "text-embedding-3-large": 3072,
    "text-embedding-ada-002": 1536,
}


def get_embedding_dimension(model_name: str | None = None) -> int:
    """
    Return the expected vector dimension for the configured
    OpenAI embedding model.
    """
    name = (
        model_name or settings.embedding_model or ""
    ).strip()

    if not name:
        raise RuntimeError("Embedding model is not configured")

    normalized = name.lower()

    if normalized in EMBEDDING_DIMENSIONS:
        return EMBEDDING_DIMENSIONS[normalized]

    raise ValueError(
        f"Unsupported embedding model '{name}'. "
        "Configure a supported OpenAI embedding model "
        "or explicitly add its verified dimension."
    )


def get_embeddings() -> OpenAIEmbeddings:
    """
    Initialize and cache the embedding model.
    """
    global _embeddings

    if _embeddings is None:
        if not settings.openai_api_key:
            raise RuntimeError("OPENAI_API_KEY is missing")

        model_name = settings.embedding_model

        # Validate the model before initializing it.
        get_embedding_dimension(model_name)

        _embeddings = OpenAIEmbeddings(
            model=model_name,
            api_key=settings.openai_api_key,
        )

    return _embeddings


def _get_index_names(client: Pinecone) -> set[str]:
    """
    Return existing Pinecone index names.

    Supports common Pinecone SDK index-list response formats.
    """
    response = client.list_indexes()

    # Newer SDK response objects may expose names().
    if callable(getattr(response, "names", None)):
        return set(response.names())

    # Other SDK response formats may expose an indexes list.
    indexes = getattr(response, "indexes", None)

    if indexes is not None:
        return {
            item["name"] if isinstance(item, dict)
            else item.name
            for item in indexes
        }

    # Compatibility with iterable responses.
    names = set()

    for item in response:
        if isinstance(item, dict):
            names.add(item["name"])
        else:
            names.add(item.name)

    return names


def ensure_index():
    """
    Verify that the Pinecone index exists and has the
    expected dimension. Create it if it does not exist.

    Existing indexes with incorrect dimensions are not
    automatically deleted.
    """
    if not settings.pinecone_api_key:
        raise RuntimeError("PINECONE_API_KEY is missing")

    if not settings.pinecone_index_name:
        raise RuntimeError("Pinecone index name is not configured")

    desired_dimension = get_embedding_dimension()

    client = Pinecone(
        api_key=settings.pinecone_api_key
    )

    index_name = settings.pinecone_index_name
    index_names = _get_index_names(client)

    if index_name in index_names:
        index_info = client.describe_index(index_name)

        if isinstance(index_info, dict):
            current_dimension = index_info.get("dimension")
        else:
            current_dimension = getattr(
                index_info, "dimension", None
            )

        if (
            current_dimension is not None
            and int(current_dimension) != desired_dimension
        ):
            raise RuntimeError(
                f"Pinecone index '{index_name}' has dimension "
                f"{current_dimension}, but embedding model "
                f"'{settings.embedding_model}' requires "
                f"{desired_dimension}. Use a separate index "
                "with the correct dimension or migrate the data."
            )

    else:
        client.create_index(
            name=index_name,
            dimension=desired_dimension,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1",
            ),
        )

        # Wait until the index is ready.
        timeout_seconds = 180
        poll_interval = 2
        elapsed = 0

        while elapsed < timeout_seconds:
            index_info = client.describe_index(index_name)

            if isinstance(index_info, dict):
                status = index_info.get("status", {})
            else:
                status = getattr(index_info, "status", {})

            if isinstance(status, dict):
                ready = status.get("ready", False)
            else:
                ready = getattr(status, "ready", False)

            if ready:
                break

            time.sleep(poll_interval)
            elapsed += poll_interval

        else:
            raise TimeoutError(
                f"Pinecone index '{index_name}' did not become "
                f"ready within {timeout_seconds} seconds."
            )

    return client.Index(index_name)


def get_vectorstore() -> PineconeVectorStore:
    """
    Initialize and cache the LangChain Pinecone vector store.
    """
    global _vectorstore

    if _vectorstore is None:
        index = ensure_index()

        _vectorstore = PineconeVectorStore(
            index=index,
            embedding=get_embeddings(),
            namespace=settings.pinecone_namespace,
        )

    return _vectorstore


def get_retriever():
    """
    Return a retriever that searches for the top-k
    relevant document chunks.
    """
    top_k = int(settings.top_k)

    if top_k < 1:
        raise ValueError("settings.top_k must be at least 1")

    return get_vectorstore().as_retriever(
        search_kwargs={"k": top_k}
    )


def add_documents(
    chunks: Iterable[Document],
    ids: list[str] | None = None,
):
    """
    Embed and store document chunks in Pinecone.

    Args:
        chunks: Document chunks from chunk_documents().
        ids: Optional stable, unique IDs for the chunks.

    Returns:
        IDs returned by the vector-store insertion operation.
    """
    chunks = list(chunks)

    if not chunks:
        return []

    store = get_vectorstore()

    if ids is not None:
        if len(ids) != len(chunks):
            raise ValueError(
                "The number of IDs must match the number of chunks."
            )

        if len(set(ids)) != len(ids):
            raise ValueError("Document IDs must be unique.")

        return store.add_documents(
            chunks=chunks,
            ids=ids,
        )

    return store.add_documents(chunks)
