from datetime import date

from pydantic import BaseModel


class BacktestRequest(BaseModel):

    scanner_id: int

    start_date: date

    end_date: date


class BacktestResponse(BaseModel):

    total_signals: int

    winners: int

    losers: int

    win_rate: float

    average_return: float
