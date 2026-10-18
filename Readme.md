# Company Agentic RAG

A small company knowledge assistant with a JavaScript UI. It searches a Pinecone
knowledge base first, asks an LLM to evaluate whether the retrieved evidence is
enough to answer, and falls back to Tavily web search when it is not. Web search
queries are rewritten using the previous evidence feedback, with a hard limit of
four attempts. If the evidence still does not support a reliable answer, the
assistant says the answer is unavailable.

## Requirements

- Python 3.10 or newer
- A Groq API key
- A Tavily API key
- A Pinecone API key and an existing index

Create the Pinecone index before starting the app. Use dimension **384**,
cosine distance, and a serverless configuration supported by your Pinecone
account. The default embedding model is
`sentence-transformers/all-MiniLM-L6-v2`.

## Run on Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
if (-not (Test-Path .env)) { Copy-Item .env.example .env }
```

Add your API keys to `.env`. Set `PINECONE_INDEX_NAME` to the index you created.
Then launch the app locally:

```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open <http://127.0.0.1:8000>. Use **Add company documents** to index PDF, DOCX,
TXT, or Markdown files, then ask questions in the assistant. Uploads are limited
to 10 files per request and 15 MB per file.

## Pipeline

1. Embed and retrieve up to five chunks from the configured Pinecone namespace.
2. Ask the Groq model to assess whether those company sources fully support an
   answer. A supported, sufficiently confident answer is returned with company
   source names.
3. Otherwise, rewrite a focused web query and search with Tavily.
4. Assess the company and web evidence together. If it is not sufficiently
   reliable, use that assessment to rewrite the next query and search again.
5. Stop as soon as evidence passes the reliability threshold, or after four
   Tavily searches. The final response includes the sources used.

The confidence thresholds are `0.75` for company-only evidence and `0.82` for
answers using web evidence; they are defined in `app/pipeline.py`.

## Deployment and data handling

This is a local prototype and does not include user authentication, role-based
access, or tenant isolation. Keep it on a trusted machine/network until those
controls are added. Uploaded document text is sent to the configured embedding
provider and stored in Pinecone; questions and evidence may be sent to Groq and,
on fallback, search queries to Tavily. Review each provider's data-handling
terms before indexing confidential company documents. API keys stay on the
server and must not be placed in frontend code.
