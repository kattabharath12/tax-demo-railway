from sqlalchemy.orm import Session
from app.payment.schemas import PaymentRequest, PaymentResponse
from datetime import datetime
import uuid

class PaymentService:
    def __init__(self, db: Session):
        self.db = db

    def process_payment(self, request: PaymentRequest) -> PaymentResponse:
        # Simulate payment processing
        payment_id = str(uuid.uuid4())

        return PaymentResponse(
            payment_id=payment_id,
            status="completed",
            amount=request.amount,
            processed_at=datetime.now()
        )
