from fastapi import APIRouter
from backend.app.core.logger import logger

router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    logger.info("Health check endpoint called")

    return {
        "status": "healthy",
        "application": "Enterprise Knowledge Assistant",
        "version": "1.0.0"
    }