from sqlalchemy.orm import Session

class AdminService:
    def __init__(self, db: Session):
        self.db = db

    def get_dashboard_stats(self):
        return {
            "total_users": 150,
            "total_submissions": 89,
            "pending_submissions": 12,
            "revenue": 15750.00
        }

    def get_users(self):
        return {
            "users": [
                {"id": 1, "email": "user1@example.com", "status": "active"},
                {"id": 2, "email": "user2@example.com", "status": "active"}
            ]
        }

    def get_submissions(self):
        return {
            "submissions": [
                {"id": 1, "user_id": 1, "status": "completed", "amount": 250.00},
                {"id": 2, "user_id": 2, "status": "pending", "amount": 180.00}
            ]
        }
