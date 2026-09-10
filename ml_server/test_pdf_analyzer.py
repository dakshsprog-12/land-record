from app.pdf.analyzer import analyze_pdf


pdf_path = "test_document.pdf"

pages = analyze_pdf(pdf_path)

for page in pages:
    print(page)