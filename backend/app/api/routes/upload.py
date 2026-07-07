from fastapi import APIRouter, UploadFile, File

from backend.app.core.logger import logger
from backend.app.services.document_service import DocumentService
from backend.app.services.parser_service import ParserService
from backend.app.services.chunk_service import ChunkService
from backend.app.services.embedding_service import EmbeddingService
from backend.app.services.vector_store_service import VectorStoreService

router = APIRouter(tags=["Upload"])


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    logger.info(f"Received file: {file.filename}")

    # Step 1: Save the uploaded file
    file_path = await DocumentService.save_document(file)
    logger.info(f"File saved successfully: {file_path}")

    try:
        # Step 2: Extract text from the document
        text = ParserService.extract_text(file_path)
        logger.info(f"Extracted {len(text)} characters")

        # Step 3: Split the text into chunks
        chunks = ChunkService.split_text(text)
        logger.info(f"Created {len(chunks)} chunks")

        # Step 4: Initialize ChromaDB
        vector_store = VectorStoreService()

        # Step 5: Generate embeddings and store each chunk
        for index, chunk in enumerate(chunks):

            embedding = EmbeddingService.generate_embedding(chunk)

            vector_store.add_document(
                chunk_id=f"{file.filename}_{index}",
                text=chunk,
                embedding=embedding,
                metadata={
                    "filename": file.filename,
                    "chunk": index
    }
)

        logger.info(f"Stored {len(chunks)} vectors in ChromaDB")

    except Exception as e:
        logger.error(f"Failed to process document: {e}")
        raise

    # Step 6: Return success response
    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "path": file_path,
        "characters": len(text),
        "chunks": len(chunks),
        "stored_vectors": len(chunks),
        "preview": chunks[0][:300] if chunks else ""
    }