from fastapi import APIRouter

from backend.app.models.chat import ChatRequest
from backend.app.services.embedding_service import EmbeddingService
from backend.app.services.search_service import SearchService
from backend.app.services.llm_service import LLMService
from backend.app.core.settings import TOP_K
from backend.app.services.citation_service import CitationService
from fastapi.responses import StreamingResponse

router = APIRouter(tags=["Chat"])

search_service = SearchService()


@router.post("/chat")
async def chat(request: ChatRequest):

    question_embedding = EmbeddingService.generate_embedding(
        request.question
    )

    results = search_service.search(
        embedding=question_embedding,
        n_results=TOP_K
    )

    context = ""

    for i, chunk in enumerate(results["documents"][0], start=1):
        context += f"Chunk {i}:\n"
        context += chunk
        context += "\n\n"

    answer = LLMService.generate_answer(
        context=context,
        question=request.question
    )

    print(results["metadatas"])
    citations = CitationService.build_citations(results)

    return {
    "question": request.question,
    "answer": answer,
    "citations": citations
    }
@router.post("/chat/stream")
async def stream_chat(request: ChatRequest):

    question_embedding = EmbeddingService.generate_embedding(
        request.question
    )

    results = search_service.search(
        embedding=question_embedding,
        n_results=TOP_K
    )

    context = ""

    for i, chunk in enumerate(results["documents"][0], start=1):
        context += f"Chunk {i}:\n"
        context += chunk
        context += "\n\n"

    return StreamingResponse(
        LLMService.stream_answer(
            context=context,
            question=request.question
        ),
        media_type="text/plain"
    )