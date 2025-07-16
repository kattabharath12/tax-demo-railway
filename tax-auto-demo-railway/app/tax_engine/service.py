from sqlalchemy.orm import Session
from app.tax_engine.schemas import TaxCalculationRequest, TaxCalculationResponse

class TaxEngineService:
    def __init__(self, db: Session):
        self.db = db

    def calculate_taxes(self, request: TaxCalculationRequest) -> TaxCalculationResponse:
        # Simplified tax calculation logic
        taxable_income = max(0, request.income - request.deductions)

        # Federal tax brackets (simplified)
        federal_tax = self._calculate_federal_tax(taxable_income, request.filing_status)

        # State tax (if applicable)
        state_tax = 0
        if request.state:
            state_tax = self._calculate_state_tax(taxable_income, request.state)

        total_tax = federal_tax + state_tax
        effective_rate = (total_tax / request.income) * 100 if request.income > 0 else 0
        marginal_rate = self._get_marginal_rate(taxable_income, request.filing_status)

        return TaxCalculationResponse(
            federal_tax=federal_tax,
            state_tax=state_tax,
            total_tax=total_tax,
            effective_rate=effective_rate,
            marginal_rate=marginal_rate
        )

    def _calculate_federal_tax(self, income: float, filing_status: str) -> float:
        # Simplified federal tax calculation
        if income <= 10275:
            return income * 0.10
        elif income <= 41775:
            return 1027.50 + (income - 10275) * 0.12
        elif income <= 89450:
            return 4807.50 + (income - 41775) * 0.22
        else:
            return 15213.50 + (income - 89450) * 0.24

    def _calculate_state_tax(self, income: float, state: str) -> float:
        # Simplified state tax calculation
        state_rates = {
            "CA": 0.08,
            "NY": 0.06
        }
        return income * state_rates.get(state, 0)

    def _get_marginal_rate(self, income: float, filing_status: str) -> float:
        if income <= 10275:
            return 10.0
        elif income <= 41775:
            return 12.0
        elif income <= 89450:
            return 22.0
        else:
            return 24.0
