from app.services.embedding_service import EmbeddingService

embedding = EmbeddingService.generate_embedding(
    "MY name is Sudhansu Sekhar Sahoo and i am a piece of shit."
)

print(type(embedding))
print(len(embedding))
print(embedding[:10])