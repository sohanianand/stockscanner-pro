from app.models.alert import Alert
from app.repositories.alert_repository import AlertRepository


class AlertService:

    def __init__(self, db):

        self.repo = AlertRepository(db)

    def create(
        self,
        user_id,
        request,
    ):

        alert = Alert(

            user_id=user_id,

            scanner_id=request.scanner_id,

            notification_type=request.notification_type,

        )

        return self.repo.create(alert)
