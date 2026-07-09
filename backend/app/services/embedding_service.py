from ollama import Client

from backend.app.core.settings import (
    EMBEDDING_MODEL,
    OLLAMA_HOST
)

client = Client(host=OLLAMA_HOST)


class EmbeddingService:

    @staticmethod
    def generate_embedding(text: str):

        response = client.embeddings(
            model=EMBEDDING_MODEL,
            prompt=text
        )

        return response["embedding"]