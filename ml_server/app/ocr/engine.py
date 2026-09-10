from paddleocr import PaddleOCR


class OCREngine:
    def __init__(self, lang="en"):
        self.ocr = PaddleOCR(
            lang=lang,
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False
        )

    def process(self, image_path, use_preprocessing=False):

        results = self.ocr.predict(image_path)

        output = []

        for result in results:
            texts = result["rec_texts"]
            scores = result["rec_scores"]
            boxes = result["rec_boxes"]

            for text, score, box in zip(texts, scores, boxes):
                output.append({
                    "text": text,
                    "confidence": float(score),
                    "bbox": box.tolist()
                })

        return output