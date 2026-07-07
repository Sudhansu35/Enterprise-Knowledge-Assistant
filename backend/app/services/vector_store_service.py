import chromadb


class VectorStoreService:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="data/chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="enterprise_documents"
        )

    def add_document(
        self,
        chunk_id: str,
        text: str,
        embedding: list,
        metadata: dict
    ):

        self.collection.add(
            ids=[chunk_id],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata]
        )

    def search(
        self,
        embedding: list,
        n_results: int = 3
    ):

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )
    def search(
        self,
        embedding: list,
        n_results: int = 3
    ):

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results
    )

        return results