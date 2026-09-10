from app.ocr.engine import OCREngine


engine = OCREngine(lang="hi")

result = engine.process(
    "upscaled.jpg",
    use_preprocessing=False
)

for item in result:
    print(item)