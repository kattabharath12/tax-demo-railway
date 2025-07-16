from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.admin.service import AdminService

router = APIRouter()

@router.get("/dashboard")
async def get_dashboard_stats(db: Session = Depends(get_db)):
    admin_service = AdminService(db)
    return admin_service.get_dashboard_stats()

@router.get("/users")
async def get_users(db: Session = Depends(get_db)):
    admin_service = AdminService(db)
    return admin_service.get_users()

@router.get("/submissions")
async def get_submissions(db: Session = Depends(get_db)):
    admin_service = AdminService(db)
    return admin_service.get_submissions()
