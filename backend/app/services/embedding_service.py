import ollama


class EmbeddingService:

    @staticmethod
    def generate_embedding(text: str):

        response = ollama.embeddings(
            model="nomic-embed-text",
            prompt=text
        )

        return response["embedding"]