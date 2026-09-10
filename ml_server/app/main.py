from fastapi import FastAPI, UploadFile, File
from app.ocr.engine import OCREngine
from app.pdf.ocr_processor import process_pdf

import os
import shutil


app = FastAPI()

ocr_engine = OCREngine(lang="hi")


@app.get("/")
def root():
    return {
        "message": "Land Record ML service is running"
    }


@app.post("/ocr")
async def process_ocr(file: UploadFile = File(...)):

    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)

    file_path = os.path.join(
        temp_dir,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    # PDF
    if extension == ".pdf":

        output_dir = os.path.join(
            temp_dir,
            "pdf_pages"
        )

        pages = process_pdf(
            file_path,
            output_dir,
            ocr_engine
        )

        return {
            "success": True,
            "filename": file.filename,
            "type": "pdf",
            "pages": pages
        }

    # Image
    if extension in [".jpg", ".jpeg", ".png", ".webp"]:

        result = ocr_engine.process(file_path)

        return {
            "success": True,
            "filename": file.filename,
            "type": "image",
            "results": result
        }

    return {
        "success": False,
        "message": "Unsupported file type"
    }