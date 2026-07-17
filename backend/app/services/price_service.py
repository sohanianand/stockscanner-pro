import yfinance as yf
from sqlalchemy.orm import Session

from app.core.logging import logger
from app.models.stock_price import StockPrice
from app.repositories.price_repository import PriceRepository


def download_history(symbol: str, db: Session):

    symbol = symbol.upper()

    logger.info("Downloading {}", symbol)

    price_repo = PriceRepository(db)

    ticker = yf.Ticker(f"{symbol}.NS")

    history = ticker.history(
        period="10y",
        auto_adjust=False
    )

    if history.empty:
        logger.warning("No data found for {}", symbol)

        return {
            "message": f"No data found for {symbol}"
        }

    existing_dates = price_repo.get_existing_dates(symbol)

    records = []

    for index, row in history.iterrows():

        trade_date = index.date()

        if trade_date in existing_dates:
            continue

        records.append(
            StockPrice(
                symbol=symbol,
                trading_date=trade_date,
                open=float(row["Open"]),
                high=float(row["High"]),
                low=float(row["Low"]),
                close=float(row["Close"]),
                adj_close=float(row["Adj Close"]),
                volume=int(row["Volume"]),
            )
        )

    if records:
        price_repo.bulk_insert(records)

    logger.info(
        "Inserted {} rows for {}",
        len(records),
        symbol,
    )

    return {
        "symbol": symbol,
        "rows_inserted": len(records),
    }
