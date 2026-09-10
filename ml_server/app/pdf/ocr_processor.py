from app.pdf.processor import convert_pdf_to_images


def process_pdf(pdf_path, output_dir, ocr_engine):
    page_images = convert_pdf_to_images(
        pdf_path,
        output_dir
    )

    pages = []

    for page_number, image_path in enumerate(page_images, start=1):
        ocr_result = ocr_engine.process(image_path)

        pages.append({
            "page": page_number,
            "image": image_path,
            "results": ocr_result
        })

    return pages