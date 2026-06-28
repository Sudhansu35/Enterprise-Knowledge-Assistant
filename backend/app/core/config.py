from pydantic import BaseModel


class Settings(BaseModel):
    APP_NAME: str = "Enterprise Knowledge Assistant"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Production Grade RAG System"

    API_PREFIX: str = "/api/v1"


settings = Settings()