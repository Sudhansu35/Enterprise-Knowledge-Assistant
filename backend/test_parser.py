from app.services.parser_service import ParserService

text = ParserService.extract_text(
    "data/raw/Sudhansu Resume (2) (2).pdf"
)

print(text)