from app.ocr.engine import OCREngine
from app.pdf.processor import convert_pdf_to_images
import os


PDF_PATH = "bhumi_rasid.pdf"
OUTPUT_DIR = "temp_layout"


os.makedirs(OUTPUT_DIR, exist_ok=True)

# Convert first PDF page to image
images = convert_pdf_to_images(PDF_PATH, OUTPUT_DIR)

image_path = images[0]

# Run OCR
ocr_engine = OCREngine(lang="hi")
results = ocr_engine.process(image_path)

# Sort by vertical position first, then horizontal position
results = sorted(
    results,
    key=lambda item: (
        item["bbox"][1],
        item["bbox"][0]
    )
)

print("\nOCR LAYOUT\n")
print("-" * 100)

for item in results:
    print(
        f"{item['bbox']} | "
        f"{item['confidence']:.3f} | "
        f"{item['text']}"
    )