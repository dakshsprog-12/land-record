import os

from app.pdf.ocr_processor import process_pdf
from app.extraction.pipeline import extract_land_record


def process_document(file_path, output_dir, ocr_engine):
    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        pages = process_pdf(
            file_path,
            output_dir,
            ocr_engine
        )

        return {
            "document_type": "pdf",
            "pages": pages
        }

    if extension in [".jpg", ".jpeg", ".png", ".webp"]:
        ocr_result = ocr_engine.process(file_path)

        result = extract_land_record(
            ocr_result
        )

        return {
            "document_type": "image",
            "result": result
        }

    return {
        "document_type": "unknown",
        "error": "Unsupported file type"
    }