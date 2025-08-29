# backend/pdf_utils.py

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """Extract raw text from PDF bytes."""
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = [page.get_text() for page in doc]
    return "\n".join(text)

def chunk_text(
    text: str, chunk_size: int = 500, overlap: int = 50
) -> list[str]:
    """
    Split text into overlapping chunks of ~chunk_size characters.
    """
    chunks = []
    start = 0
    length = len(text)
    while start < length:
        end = min(start + chunk_size, length)
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks