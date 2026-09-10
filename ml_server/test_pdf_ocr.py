from app.ocr.engine import OCREngine
from app.pdf.ocr_processor import process_pdf


ocr_engine = OCREngine(lang="hi")

pdf_path = "bhumi_rasid.pdf"
output_dir = "pdf_pages"

result = process_pdf(
    pdf_path,
    output_dir,
    ocr_engine
)

for page in result:
    print(f"\n===== PAGE {page['page']} =====")

    for item in page["results"]:
        print(
            item["text"],
            "|",
            item["confidence"]
        )