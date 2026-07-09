import os
from dotenv import load_dotenv

OLLAMA_HOST = os.getenv(
    "OLLAMA_HOST",
    "http://localhost:11434"
)
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Enterprise Knowledge Assistant")
VERSION = os.getenv("VERSION", "1.0.0")
DESCRIPTION = os.getenv("DESCRIPTION", "Production Grade RAG System")

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))

LLM_MODEL = os.getenv("OLLAMA_MODEL", "llama3")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
TOP_K = int(os.getenv("TOP_K", 5))
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "enterprise_documents")