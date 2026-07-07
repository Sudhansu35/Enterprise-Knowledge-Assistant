from fastapi import APIRouter

from backend.app.models.chat import ChatRequest
from backend.app.services.embedding_service import EmbeddingService
from backend.app.services.vector_store_service import VectorStoreService
from backend.app.services.llm_service import LLMService

router = APIRouter(tags=["Chat"])

vector_store = VectorStoreService()


@router.post("/chat")
async def chat(request: ChatRequest):

    question_embedding = EmbeddingService.generate_embedding(
        request.question
    )

    results = vector_store.search(
        embedding=question_embedding,
        n_results=3
    )

    context = "\n\n".join(results["documents"][0])

    answer = LLMService.generate_answer(
        context=context,
        question=request.question
    )

    print(results["metadatas"])

    return {
        "question": request.question,
        "answer": answer,
        "sources": results["documents"][0],
        "metadata": results["metadatas"][0]
    }