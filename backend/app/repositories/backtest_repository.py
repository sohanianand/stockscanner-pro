from sqlalchemy.orm import Session

from app.models.backtest import Backtest


class BacktestRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(self, obj):

        self.db.add(obj)

        self.db.commit()

        self.db.refresh(obj)

        return obj
