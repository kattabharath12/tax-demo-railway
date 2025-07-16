import os
import shutil
from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.core.config import settings

class FileService:
    def __init__(self, db: Session):
        self.db = db
        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    async def upload_file(self, file: UploadFile):
        if file.size > settings.MAX_FILE_SIZE:
            raise HTTPException(status_code=413, detail="File too large")

        file_path = os.path.join(settings.UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {
            "filename": file.filename,
            "size": file.size,
            "content_type": file.content_type,
            "path": file_path
        }

    def list_files(self):
        files = []
        for filename in os.listdir(settings.UPLOAD_DIR):
            file_path = os.path.join(settings.UPLOAD_DIR, filename)
            if os.path.isfile(file_path):
                files.append({
                    "filename": filename,
                    "size": os.path.getsize(file_path)
                })
        return files
