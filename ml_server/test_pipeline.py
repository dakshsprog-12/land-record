from app.ocr.engine import OCREngine
from app.extraction.pipeline import extract_land_record


engine = OCREngine(lang="hi")

ocr_results = engine.process("bhumi_rasid.jpeg")

result = extract_land_record(ocr_results)

print(result)