from fastapi import APIRouter

from backend.app.core.logger import logger

router = APIRouter()


@router.get("/", tags=["Home"])
def home():
    logger.info("Home endpoint called")
    logger.info("Sending welcome response")

    return {
        "message": "Welcome to Enterprise Knowledge Assistant is HERE"
    }