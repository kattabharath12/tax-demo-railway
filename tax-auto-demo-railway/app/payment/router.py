from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.payment.service import PaymentService
from app.payment.schemas import PaymentRequest, PaymentResponse

router = APIRouter()

@router.post("/process", response_model=PaymentResponse)
async def process_payment(request: PaymentRequest, db: Session = Depends(get_db)):
    payment_service = PaymentService(db)
    return payment_service.process_payment(request)

@router.get("/methods")
async def get_payment_methods():
    return {
        "methods": ["credit_card", "bank_transfer", "ach"],
        "supported_cards": ["visa", "mastercard", "amex"]
    }
