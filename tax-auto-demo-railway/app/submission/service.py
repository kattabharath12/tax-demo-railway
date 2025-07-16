from sqlalchemy.orm import Session
from app.submission.schemas import SubmissionRequest, SubmissionResponse
from datetime import datetime
import uuid

class SubmissionService:
    def __init__(self, db: Session):
        self.db = db

    def submit_return(self, request: SubmissionRequest) -> SubmissionResponse:
        # Simulate submission process
        submission_id = hash(str(request.user_id) + str(datetime.now())) % 1000000
        confirmation_number = str(uuid.uuid4())[:8].upper()

        return SubmissionResponse(
            submission_id=submission_id,
            status="submitted",
            submitted_at=datetime.now(),
            confirmation_number=confirmation_number
        )

    def get_status(self, submission_id: int):
        return {
            "submission_id": submission_id,
            "status": "processing",
            "last_updated": datetime.now()
        }

    def get_history(self):
        return {
            "submissions": [
                {
                    "submission_id": 123456,
                    "status": "accepted",
                    "submitted_at": "2023-12-01T10:00:00Z"
                }
            ]
        }
