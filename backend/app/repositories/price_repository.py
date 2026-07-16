from datetime import date

from sqlalchemy.orm import Session

from app.models.price import StockPrice


class PriceRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_prices(self, prices: list[StockPrice]):
        """
        Save multiple price records.
        """
        self.db.bulk_save_objects(prices)
        self.db.commit()

    def delete_symbol(self, symbol: str):
        """
        Delete all historical prices for a symbol.
        """
        self.db.query(StockPrice).filter(
            StockPrice.symbol == symbol
        ).delete()

        self.db.commit()

    def get_history(
        self,
        symbol: str,
        start_date: date | None = None,
        end_date: date | None = None,
    ):
        """
        Return historical prices.
        """
        query = self.db.query(StockPrice).filter(
            StockPrice.symbol == symbol
        )

        if start_date:
            query = query.filter(StockPrice.trading_date >= start_date)

        if end_date:
            query = query.filter(StockPrice.trading_date <= end_date)

        return query.order_by(StockPrice.trading_date.asc()).all()

    def get_latest_price(self, symbol: str):
        """
        Return latest price for a symbol.
        """
        return (
            self.db.query(StockPrice)
            .filter(StockPrice.symbol == symbol)
            .order_by(StockPrice.trading_date.desc())
            .first()
        )

    def symbol_exists(self, symbol: str):
        """
        Check whether price history exists.
        """
        return (
            self.db.query(StockPrice)
            .filter(StockPrice.symbol == symbol)
            .first()
            is not None
        )

    def get_symbols(self):
        """
        Return all symbols.
        """
        rows = (
            self.db.query(StockPrice.symbol)
            .distinct()
            .order_by(StockPrice.symbol)
            .all()
        )

        return [row[0] for row in rows]

    def get_existing_dates(self, symbol: str):
        """
        Return all existing trading dates for a symbol.
        """
        rows = (
            self.db.query(StockPrice.trading_date)
            .filter(StockPrice.symbol == symbol)
            .all()
        )

        return {row[0] for row in rows}
