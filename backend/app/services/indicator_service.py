import pandas as pd
import ta

from sqlalchemy.orm import Session

from app.models.stock_price import StockPrice
from app.models.indicator import Indicator


def calculate_indicators(symbol: str, db: Session):

    prices = (
        db.query(StockPrice)
        .filter(StockPrice.symbol == symbol)
        .order_by(StockPrice.trading_date)
        .all()
    )

    if not prices:
        return {"message": "No price data"}

    df = pd.DataFrame([
        {
            "date": p.trading_date,
            "close": p.close,
            "high": p.high,
            "low": p.low,
            "volume": p.volume,
        }
        for p in prices
    ])

    df["ema20"] = ta.trend.ema_indicator(df["close"], window=20)
    df["ema50"] = ta.trend.ema_indicator(df["close"], window=50)

    df["sma20"] = ta.trend.sma_indicator(df["close"], window=20)

    df["rsi"] = ta.momentum.rsi(df["close"], window=14)

    macd = ta.trend.MACD(df["close"])

    df["macd"] = macd.macd()
    df["signal"] = macd.macd_signal()
    df["hist"] = macd.macd_diff()

    bb = ta.volatility.BollingerBands(df["close"])

    df["upper"] = bb.bollinger_hband()
    df["middle"] = bb.bollinger_mavg()
    df["lower"] = bb.bollinger_lband()

    db.query(Indicator).filter(
        Indicator.symbol == symbol
    ).delete()

    for _, row in df.iterrows():

        db.add(
            Indicator(
                symbol=symbol,
                trading_date=row["date"],
                close=row["close"],
                ema20=row["ema20"],
                ema50=row["ema50"],
                sma20=row["sma20"],
                rsi=row["rsi"],
                macd=row["macd"],
                macd_signal=row["signal"],
                macd_histogram=row["hist"],
                bb_upper=row["upper"],
                bb_middle=row["middle"],
                bb_lower=row["lower"],
            )
        )

    db.commit()

    return {
        "symbol": symbol,
        "rows": len(df)
    }
