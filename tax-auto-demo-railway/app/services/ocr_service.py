import pytesseract
from PIL import Image
from fastapi import UploadFile, HTTPException
import io

class OCRService:
    def __init__(self):
        pass

    async def extract_text(self, file: UploadFile):
        try:
            # Read the uploaded file
            contents = await file.read()
            image = Image.open(io.BytesIO(contents))

            # Extract text using OCR
            text = pytesseract.image_to_string(image)

            return {
                "filename": file.filename,
                "extracted_text": text,
                "status": "success"
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"OCR processing failed: {str(e)}")
