from pydantic import BaseModel
from datetime import datetime

class PaymentRequest(BaseModel):
    amount: float
    payment_method: str
    card_token: str

class PaymentResponse(BaseModel):
    payment_id: str
    status: str
    amount: float
    processed_at: datetime
