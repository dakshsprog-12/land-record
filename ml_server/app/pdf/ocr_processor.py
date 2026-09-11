import os

from app.pdf.processor import convert_pdf_to_images
from app.pdf.analyzer import analyze_pdf
from app.pdf.text_extractor import extract_text_from_pdf
from app.extraction.pipeline import extract_land_record
from app.extraction.text_pipeline import extract_land_record_from_text


def process_pdf(pdf_path, output_dir, ocr_engine):

    analysis = analyze_pdf(pdf_path)

    text_pages = extract_text_from_pdf(pdf_path)

    pages = []

    scanned_pages = [
        page["page"]
        for page in analysis
        if not page["has_text"]
    ]

    # Only render pages that need OCR
    if scanned_pages:
        all_images = convert_pdf_to_images(
            pdf_path,
            output_dir
        )

        image_map = {
            index + 1: path
            for index, path in enumerate(all_images)
        }
    else:
        image_map = {}

    for page_info, text_info in zip(analysis, text_pages):

        page_number = page_info["page"]

        if page_info["has_text"]:
            result = extract_land_record_from_text(
                text_info["text"]
            )
            pages.append({
                "page": page_number,
                "source": "text",
                "text": text_info["text"],
                "result": result
            })

        else:

            image_path = image_map[page_number]

            ocr_result = ocr_engine.process(
                image_path
            )

            result = extract_land_record(
                ocr_result
            )

            pages.append({
                "page": page_number,
                "source": "ocr",
                "image": image_path,
                "result": result
            })

    return pages