from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.submission.service import SubmissionService
from app.submission.schemas import SubmissionRequest, SubmissionResponse

router = APIRouter()

@router.post("/submit", response_model=SubmissionResponse)
async def submit_tax_return(request: SubmissionRequest, db: Session = Depends(get_db)):
    submission_service = SubmissionService(db)
    return submission_service.submit_return(request)

@router.get("/status/{submission_id}")
async def get_submission_status(submission_id: int, db: Session = Depends(get_db)):
    submission_service = SubmissionService(db)
    return submission_service.get_status(submission_id)

@router.get("/history")
async def get_submission_history(db: Session = Depends(get_db)):
    submission_service = SubmissionService(db)
    return submission_service.get_history()
