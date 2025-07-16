from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.file_service import FileService
from app.services.ocr_service import OCRService

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_service = FileService(db)
    return await file_service.upload_file(file)

@router.post("/ocr")
async def process_ocr(file: UploadFile = File(...)):
    ocr_service = OCRService()
    return await ocr_service.extract_text(file)

@router.get("/files")
async def list_files(db: Session = Depends(get_db)):
    file_service = FileService(db)
    return file_service.list_files()
