from fastapi import FastAPI, UploadFile, File
from app.ocr.engine import OCREngine

app = FastAPI()

ocr_engine = OCREngine()


@app.get("/")
def root():
    return {
        "message": "Land Record ML service is running"
    }


@app.post("/ocr")
async def process_ocr(file: UploadFile = File(...)):

    contents = await file.read()

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as f:
        f.write(contents)

    result = ocr_engine.process(temp_path)

    return {
        "success": True,
        "filename": file.filename,
        "results": result
    }