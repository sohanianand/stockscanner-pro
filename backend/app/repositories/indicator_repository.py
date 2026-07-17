from sqlalchemy.orm import Session

from app.models.indicator import Indicator
from app.repositories.base_repository import BaseRepository


class IndicatorRepository(BaseRepository[Indicator]):

    def __init__(self, db: Session):
        super().__init__(Indicator, db)

    def delete_by_symbol(self, symbol: str):
        (
            self.db.query(Indicator)
            .filter(Indicator.symbol == symbol)
            .delete()
        )
        self.db.commit()

    def bulk_insert(self, records):
        self.db.bulk_save_objects(records)
        self.db.commit()

    def latest(self, symbol: str):
        return (
            self.db.query(Indicator)
            .filter(
                Indicator.symbol == symbol
            )
            .order_by(
                Indicator.trading_date.desc()
            )
            .first()
        )
