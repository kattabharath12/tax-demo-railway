from pydantic import BaseModel
from typing import Optional, Dict, Any

class TaxCalculationRequest(BaseModel):
    filing_status: str
    income: float
    deductions: Optional[float] = 0
    state: Optional[str] = None
    additional_data: Optional[Dict[str, Any]] = {}

class TaxCalculationResponse(BaseModel):
    federal_tax: float
    state_tax: Optional[float] = 0
    total_tax: float
    effective_rate: float
    marginal_rate: float
    refund_amount: Optional[float] = 0
