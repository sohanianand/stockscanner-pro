from sqlalchemy.orm import Session

from app.models.indicator import Indicator
from app.models.latest_indicator import LatestIndicator


def update_latest(symbol: str, db: Session):

    latest = (
        db.query(Indicator)
        .filter(
            Indicator.symbol == symbol
        )
        .order_by(
            Indicator.trading_date.desc()
        )
        .first()
    )

    if latest is None:
        return {
            "message": "Indicator not found"
        }

    existing = (
        db.query(LatestIndicator)
        .filter(
            LatestIndicator.symbol == symbol
        )
        .first()
    )

    if existing:

        existing.trading_date = latest.trading_date
        existing.close = latest.close

        existing.ema20 = latest.ema20
        existing.ema50 = latest.ema50
        existing.sma20 = latest.sma20

        existing.rsi = latest.rsi

        existing.macd = latest.macd
        existing.macd_signal = latest.macd_signal
        existing.macd_histogram = latest.macd_histogram

        existing.bb_upper = latest.bb_upper
        existing.bb_middle = latest.bb_middle
        existing.bb_lower = latest.bb_lower

    else:

        db.add(
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

    db.commit()

    return {
        "symbol": symbol,
        "status": "updated"
    }
