from pathlib import Path
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = Path("data/raw")

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt", ".md"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


class DocumentService:

    @staticmethod
    async def save_document(file: UploadFile):

        extension = Path(file.filename).suffix.lower()

        if extension not in ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail="Only PDF, DOCX, TXT, and MD files are allowed."
            )

        UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

        file_path = UPLOAD_DIR / file.filename

        content = await file.read()
        if len(content) > MAX_FILE_SIZE:
            raise HTTPException(
        status_code=400,
        detail="File size exceeds the maximum limit of 10 MB."
    )

        with open(file_path, "wb") as f:
            f.write(content)

        return str(file_path)