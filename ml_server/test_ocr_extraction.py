from app.ocr.engine import OCREngine
from app.extraction.land_record import extract_land_record_fields


image_path = "bhumi_rasid.jpeg"

ocr_engine = OCREngine(lang="hi")

ocr_results = ocr_engine.process(image_path)


# Combine OCR text
text = "\n".join(
    item["text"]
    for item in ocr_results
)


print("\n===== OCR TEXT =====\n")
print(text)


# Extract fields
fields = extract_land_record_fields(text)


print("\n===== EXTRACTED FIELDS =====\n")

for field, value in fields.items():
    print(f"{field}: {value}")