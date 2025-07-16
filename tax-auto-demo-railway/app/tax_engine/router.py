from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.tax_engine.service import TaxEngineService
from app.tax_engine.schemas import TaxCalculationRequest, TaxCalculationResponse

router = APIRouter()

@router.post("/calculate", response_model=TaxCalculationResponse)
async def calculate_taxes(request: TaxCalculationRequest, db: Session = Depends(get_db)):
    tax_service = TaxEngineService(db)
    return tax_service.calculate_taxes(request)

@router.get("/forms")
async def get_supported_forms():
    return {
        "supported_forms": ["1040", "1040EZ", "1040A"],
        "states": ["CA", "NY"]
    }

@router.get("/deductions")
async def get_standard_deductions():
    return {
        "2023": {
            "single": 13850,
            "married_filing_jointly": 27700,
            "married_filing_separately": 13850,
            "head_of_household": 20800
        }
    }
