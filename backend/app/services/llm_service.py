import ollama

from backend.app.prompts.rag_prompt import RAG_PROMPT
from backend.app.core.settings import LLM_MODEL
from backend.app.services.memory_service import MemoryService
memory = MemoryService()
class LLMService:
    
    @staticmethod
    def generate_answer(context: str, question: str):

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        memory.add_message("user", prompt)

        response = ollama.chat(
            model=LLM_MODEL,
            messages=memory.get_messages()
            )

        memory.add_message(
            "assistant",
            response["message"]["content"]
        )
       

        return response["message"]["content"]