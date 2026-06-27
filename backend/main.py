from fastapi import FastAPI
from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Knowledge Assistant",
    description="Production Grade RAG System",
    version="1.0.0"
)
@app.get("/")
def home():
        return {"message": "Welcome to Enterprise Knowledge Assistant"}