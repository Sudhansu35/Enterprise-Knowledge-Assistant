import chromadb

from backend.app.core.settings import COLLECTION_NAME


class VectorStoreService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="data/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
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
        n_results: int = 3,
        where=None
    ):

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results,
            where=where
        )

        return results