from fastapi import APIRouter, UploadFile, File

from backend.app.services.document_service import DocumentService
from backend.app.services.parser_service import ParserService
from backend.app.services.chunk_service import ChunkService
from backend.app.core.logger import logger

router = APIRouter(tags=["Upload"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    logger.info(f"Received file: {file.filename}")

    # Save the uploaded file
    file_path = await DocumentService.save_document(file)
    logger.info(f"File saved successfully: {file_path}")

    try:
        # Extract text from the document
        text = ParserService.extract_text(file_path)
        logger.info(f"Extracted {len(text)} characters")

        # Split the text into chunks
        chunks = ChunkService.split_text(text)
        logger.info(f"Created {len(chunks)} chunks")

    except Exception as e:
        logger.error(f"Failed to process document: {e}")
        raise

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "path": file_path,
        "characters": len(text),
        "chunks": len(chunks),
        "preview": chunks[0][:300] if chunks else ""
    }