import ollama
from ollama import Client

from backend.app.prompts.rag_prompt import RAG_PROMPT
from backend.app.core.settings import LLM_MODEL
from backend.app.services.memory_service import MemoryService

memory = MemoryService()

client = Client(
    host="http://host.docker.internal:11434"
)
class LLMService:

    @staticmethod
    def generate_answer(context: str, question: str):

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        memory.add_message("user", prompt)

        response = client.chat(
            model=LLM_MODEL,
            messages=memory.get_messages()
        )

        memory.add_message(
            "assistant",
            response["message"]["content"]
        )

        return response["message"]["content"]

    @staticmethod
    def stream_answer(context: str, question: str):

        prompt = RAG_PROMPT.format(
            context=context,
            question=question
        )

        memory.add_message("user", prompt)

        stream = client.chat(
            model=LLM_MODEL,
            messages=memory.get_messages(),
            stream=True
        )

        full_response = ""

        for chunk in stream:

            content = chunk["message"]["content"]

            full_response += content

            yield content

        memory.add_message(
            "assistant",
            full_response
        )