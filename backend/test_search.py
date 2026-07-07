from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService

vector_store = VectorStoreService()

# This is the user's question 👇
question = "How do I build backend APIs?"

# Convert the question into an embedding
question_embedding = EmbeddingService.generate_embedding(question)

# Search ChromaDB
results = vector_store.search(
    embedding=question_embedding,
    n_results=2
)

print(results)