from sqlalchemy.orm import Session

from app.models.latest_indicator import LatestIndicator


class LatestIndicatorRepository:

    def __init__(self, db: Session):
        self.db = db

    def get(self, symbol: str):

        return (
            self.db.query(LatestIndicator)
            .filter(
                LatestIndicator.symbol == symbol
            )
            .first()
        )

    def create(self, obj):

        self.db.add(obj)

        self.db.commit()

        self.db.refresh(obj)

        return obj

    def commit(self):

        self.db.commit()
