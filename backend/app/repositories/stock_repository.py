from sqlalchemy.orm import Session

from app.models.stock import Stock

from app.repositories.base_repository import BaseRepository


class StockRepository(
    BaseRepository[Stock]
):

    def __init__(
        self,
        db: Session
    ):

        super().__init__(
            Stock,
            db
        )

    def get_by_symbol(
        self,
        symbol: str
    ):

        return (

            self.db.query(Stock)

            .filter(
                Stock.symbol == symbol
            )

            .first()

        )

    def get_all_symbols(self):

        return (

            self.db.query(
                Stock.symbol
            )

            .all()

        )
