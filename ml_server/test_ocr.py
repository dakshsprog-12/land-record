from app.ocr.engine import OCREngine


engine = OCREngine()

result = engine.process("img.webp")

for res in result:
    res.print()