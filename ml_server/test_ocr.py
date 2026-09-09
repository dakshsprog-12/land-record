from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="en"
)

result = ocr.predict("img3.jpeg")

for res in result:
    res.print()