from app.services.embedding_service import EmbeddingService
from app.services.vector_store_service import VectorStoreService

vector_store = VectorStoreService()

text = "Python is a programming language."
text = "My Name is Sudhansu."
text="C++ is a Programming Language"

embedding = EmbeddingService.generate_embedding(text)

vector_store.add_document(
    chunk_id="chunk_1",
    text=text,
    embedding=embedding
)

print("Document stored successfully!")