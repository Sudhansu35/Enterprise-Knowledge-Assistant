from app.services.llm_service import LLMService

context = """
FastAPI is a modern Python web framework.
It is used to build REST APIs.
"""

question = "What is FastAPI used for?"

answer = LLMService.generate_answer(
    context=context,
    question=question
)

print("\nAnswer:\n")
print(answer)