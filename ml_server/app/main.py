from fastapi import FastAPI, UploadFile, File
from app.ocr.engine import OCREngine
from app.document.processor import process_document

import os
import shutil


app = FastAPI()

ocr_engine = OCREngine(lang="hi")


@app.get("/")
def root():
    return {
        "message": "Land record ML service is running"
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
        shutil.copyfileobj(
            file.file,
            buffer
        )

    output_dir = os.path.join(
        temp_dir,
        "pdf_pages"
    )

    result = process_document(
        file_path,
        output_dir,
        ocr_engine
    )

    return {
        "success": True,
        "filename": file.filename,
        **result
    }