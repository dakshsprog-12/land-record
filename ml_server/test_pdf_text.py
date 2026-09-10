from app.pdf.text_extractor import extract_text_from_pdf


pdf_path = "nikhil.pdf"

pages = extract_text_from_pdf(pdf_path)

for page in pages:
    print(f"\n===== PAGE {page['page']} =====")
    print(page["text"])