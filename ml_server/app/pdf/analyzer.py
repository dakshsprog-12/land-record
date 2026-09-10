import fitz  # PyMuPDF


def analyze_pdf(pdf_path):

    pdf = fitz.open(pdf_path)

    pages = []

    for page_number, page in enumerate(pdf, start=1):

        text = page.get_text("text").strip()

        pages.append({
            "page": page_number,
            "has_text": bool(text),
            "text_length": len(text)
        })

    pdf.close()

    return pages