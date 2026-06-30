from pathlib import Path
from pypdf import PdfReader


class ParserService:

    @staticmethod
    def extract_text(file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return ParserService._extract_pdf(file_path)

        elif extension == ".txt":
            return Path(file_path).read_text(encoding="utf-8")

        elif extension == ".md":
            return Path(file_path).read_text(encoding="utf-8")

        else:
            raise ValueError(f"Unsupported file type: {extension}")
    @staticmethod
    def _extract_pdf(file_path: str) -> str:

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text 