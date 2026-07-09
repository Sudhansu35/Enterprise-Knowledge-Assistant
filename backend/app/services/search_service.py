from backend.app.services.vector_store_service import VectorStoreService
from backend.app.services.rerank_service import RerankService
from backend.app.core.logger import logger
from backend.app.services.deduplication_service import DeduplicationService


class SearchService:

    def __init__(self):
        self.vector_store = VectorStoreService()

    def search(
    self,
    embedding,
    n_results,
    where=None
    ):

        logger.info("Searching ChromaDB...")

        results = self.vector_store.search(
            embedding=embedding,
            n_results=n_results,
            where=where
        )

        logger.info(f"Retrieved {len(results['documents'][0])} chunks")

        results = RerankService.rerank(results)
        results = DeduplicationService.remove_duplicates(results)

        logger.info("Reranking completed")

        return results