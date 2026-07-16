from sqlalchemy.orm import Session

from app.models.latest_indicator import LatestIndicator

from app.repositories.indicator_repository import IndicatorRepository
from app.repositories.latest_indicator_repository import (
    LatestIndicatorRepository,
)


def update_latest(symbol: str, db: Session):

    symbol = symbol.upper()

    indicator_repo = IndicatorRepository(db)

    latest_repo = LatestIndicatorRepository(db)

    latest = indicator_repo.latest(symbol)

    if latest is None:

        return {
            "message": "Indicator not found"
        }

    current = latest_repo.get(symbol)

    if current is None:

        latest_repo.create(

            LatestIndicator(

                symbol=latest.symbol,

                trading_date=latest.trading_date,

                close=latest.close,

                ema20=latest.ema20,

                ema50=latest.ema50,

                sma20=latest.sma20,

                rsi=latest.rsi,

                macd=latest.macd,

                macd_signal=latest.macd_signal,

                macd_histogram=latest.macd_histogram,

                bb_upper=latest.bb_upper,

                bb_middle=latest.bb_middle,

                bb_lower=latest.bb_lower,

            )

        )

    else:

        current.trading_date = latest.trading_date

        current.close = latest.close

        current.ema20 = latest.ema20

        current.ema50 = latest.ema50

        current.sma20 = latest.sma20

        current.rsi = latest.rsi

        current.macd = latest.macd

        current.macd_signal = latest.macd_signal

        current.macd_histogram = latest.macd_histogram

        current.bb_upper = latest.bb_upper

        current.bb_middle = latest.bb_middle

        current.bb_lower = latest.bb_lower

        latest_repo.commit()

    return {
        "symbol": symbol,
        "status": "updated"
    }
