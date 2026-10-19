from app.services.ingestion import load_file, chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents



docs  = load_file(Path("data/kb_store/company_handbook_it.md"))

chunks = chunk_documents(docs)


print(len(chunks))
add_documents(chunks)