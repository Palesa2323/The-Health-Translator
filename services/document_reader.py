from io import BytesIO
from pathlib import Path

from PIL import Image
from pypdf import PdfReader
import pytesseract


def extract_text(uploaded_file) -> dict:
    """Extract readable text from a PDF or image upload."""

    file_name = uploaded_file.name.lower()
    file_bytes = uploaded_file.getvalue()

    if not file_bytes:
        return {
            "success": False,
            "text": "",
            "message": "The uploaded file is empty.",
        }

    try:
        if file_name.endswith(".pdf"):
            reader = PdfReader(BytesIO(file_bytes))

            if reader.is_encrypted:
                return {
                    "success": False,
                    "text": "",
                    "message": (
                        "This PDF is password-protected. "
                        "Please upload an accessible copy."
                    ),
                }

            pages = [
                page.extract_text() or ""
                for page in reader.pages
            ]

            extracted_text = "\n".join(pages).strip()

        elif Path(file_name).suffix in {".png", ".jpg", ".jpeg"}:
            image = Image.open(BytesIO(file_bytes))
            extracted_text = pytesseract.image_to_string(
                image
            ).strip()

        else:
            return {
                "success": False,
                "text": "",
                "message": "This file type is not supported.",
            }

        if not extracted_text:
            return {
                "success": False,
                "text": "",
                "message": (
                    "No readable text was found. The report may "
                    "be scanned, unclear, or contain unsupported "
                    "content. Try a clearer file or enter the "
                    "results manually."
                ),
            }

        return {
            "success": True,
            "text": extracted_text,
            "message": "Text extracted. Please verify it.",
        }

    except Exception:
        return {
            "success": False,
            "text": "",
            "message": (
                "We couldn't read this file. Please try another "
                "copy or enter the results manually."
            ),
        }