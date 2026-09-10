import fitz


def extract_text_from_pdf(pdf_path):

    pdf = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(pdf, start=1):

        text = page.get_text("text").strip()

        pages.append({
            "page": page_number,
            "text": text
        })

    pdf.close()

    return pages