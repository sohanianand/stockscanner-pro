import requests
from sqlalchemy.orm import Session

from app.models.stock import Stock

NSE_API = "https://www.nseindia.com/api/market-data-pre-open?key=ALL"

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json,text/plain,*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/",
}


def fetch_nse_stocks():
    session = requests.Session()

    # Get cookies
    session.get(
        "https://www.nseindia.com",
        headers=HEADERS,
        timeout=15,
    )

    response = session.get(
        NSE_API,
        headers=HEADERS,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    stocks = []

    for item in data.get("data", []):

        meta = item.get("metadata", {})

        symbol = meta.get("symbol")

        if not symbol:
            continue

        stocks.append(
            {
                "symbol": symbol,
                "company_name": meta.get("companyName"),
                "exchange": "NSE",
                "sector": None,
                "industry": None,
                "isin": meta.get("isin"),
            }
        )

    return stocks


def import_nse_stocks(db: Session):

    stocks = fetch_nse_stocks()

    inserted = 0
    updated = 0

    for stock in stocks:

        existing = (
            db.query(Stock)
            .filter(Stock.symbol == stock["symbol"])
            .first()
        )

        if existing:

            existing.company_name = stock["company_name"]
            existing.exchange = stock["exchange"]
            existing.sector = stock["sector"]
            existing.industry = stock["industry"]
            existing.isin = stock["isin"]

            updated += 1

        else:

            db.add(
                Stock(
                    symbol=stock["symbol"],
                    company_name=stock["company_name"],
                    exchange=stock["exchange"],
                    sector=stock["sector"],
                    industry=stock["industry"],
                    isin=stock["isin"],
                )
            )

            inserted += 1

    db.commit()

    return {
        "inserted": inserted,
        "updated": updated,
        "total": len(stocks),
    }
