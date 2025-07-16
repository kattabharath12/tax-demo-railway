from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.state.service import StateService

router = APIRouter()

@router.get("/supported")
async def get_supported_states():
    state_service = StateService()
    return state_service.get_supported_states()

@router.get("/{state_code}/requirements")
async def get_state_requirements(state_code: str):
    state_service = StateService()
    return state_service.get_state_requirements(state_code)

@router.get("/{state_code}/tax-rates")
async def get_state_tax_rates(state_code: str):
    state_service = StateService()
    return state_service.get_tax_rates(state_code)
