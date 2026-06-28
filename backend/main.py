from fastapi import FastAPI

from backend.app.api.router import router
from backend.app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
)

app.include_router(router)