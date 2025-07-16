from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class SubmissionRequest(BaseModel):
    user_id: int
    tax_data: Dict[str, Any]
    form_type: str = "1040"
    state: Optional[str] = None

class SubmissionResponse(BaseModel):
    submission_id: int
    status: str
    submitted_at: datetime
    confirmation_number: Optional[str] = None
