from sqlalchemy.orm import Session

from app.models.alert import Alert


class AlertRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(self, alert: Alert):

        self.db.add(alert)

        self.db.commit()

        self.db.refresh(alert)

        return alert

    def all_enabled(self):

        return (
            self.db.query(Alert)
            .filter(Alert.enabled == True)
            .all()
        )

    def delete(self, alert):

        self.db.delete(alert)

        self.db.commit()
