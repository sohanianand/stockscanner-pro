from datetime import date

from pydantic import BaseModel


class StockPriceResponse(BaseModel):

    symbol: str

    trading_date: date

    open: float

    high: float

    low: float

    close: float

    adj_close: float

    volume: int

    class Config:
        from_attributes = True
