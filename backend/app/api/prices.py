from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.stock_price import StockPrice
from app.services.price_service import download_history

router = APIRouter(
    prefix="/prices",
    tags=["Prices"]
)


@router.post("/{symbol}")
def download_stock_price(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Download stock price history from Yahoo Finance
    and save it into the database.
    """
    return download_history(
        symbol.upper(),
        db
    )


@router.get("/{symbol}")
def get_stock_price(
    symbol: str,
    db: Session = Depends(get_db)
):
    """
    Return all stored price history for a stock.
    """

    prices = (
        db.query(StockPrice)
        .filter(
            StockPrice.symbol == symbol.upper()
        )
        .order_by(
            StockPrice.trading_date.desc()
        )
        .all()
    )

    if not prices:
        return {
            "message": f"No data found for {symbol.upper()}"
        }

    return [
        {
            "symbol": p.symbol,
            "date": p.trading_date,
            "open": p.open,
            "high": p.high,
            "low": p.low,
            "close": p.close,
            "adj_close": p.adj_close,
            "volume": p.volume
        }
        for p in prices
    ]
