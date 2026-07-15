import yfinance as yf

from sqlalchemy.orm import Session

from app.models.stock_price import StockPrice


def download_history(symbol: str, db: Session):

    ticker = yf.Ticker(f"{symbol}.NS")

    history = ticker.history(
        period="10y",
        auto_adjust=False
    )

    if history.empty:
        return {
            "message": f"No data found for {symbol}"
        }

    inserted = 0

    for index, row in history.iterrows():

        exists = (
            db.query(StockPrice)
            .filter(
                StockPrice.symbol == symbol,
                StockPrice.trading_date == index.date()
            )
            .first()
        )

        if exists:
            continue

        price = StockPrice(

            symbol=symbol,

            trading_date=index.date(),

            open=float(row["Open"]),

            high=float(row["High"]),

            low=float(row["Low"]),

            close=float(row["Close"]),

            adj_close=float(row["Adj Close"]),

            volume=int(row["Volume"])
        )

        db.add(price)

        inserted += 1

    db.commit()

    return {
        "symbol": symbol,
        "rows_inserted": inserted
    }
