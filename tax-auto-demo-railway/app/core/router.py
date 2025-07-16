from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter()

@router.get("/status")
async def get_status():
    return {"status": "Core service is running"}

@router.get("/info")
async def get_app_info():
    return {
        "app_name": "Auto Tax Filing Demo",
        "version": "1.0.0",
        "features": [
            "IRS Form 1040 support",
            "State filing (CA, NY)",
            "Document upload & OCR",
            "Payment processing",
            "Admin dashboard"
        ]
    }
