import io
import zipfile

import pandas as pd
import requests
from sqlalchemy.orm import Session

from app.models.stock import Stock

NSE_SECURITY_URL = (
    "https://nsearchives.nseindia.com/content/cm/NSE_CM_security.csv.gz"
)


def import_nse_stocks(db: Session):

    print("Downloading NSE Security Master...")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        NSE_SECURITY_URL,
        headers=headers,
        timeout=60
    )

    response.raise_for_status()

    df = pd.read_csv(io.BytesIO(response.content), compression="gzip")

    added = 0
    updated = 0

    for _, row in df.iterrows():

        symbol = str(row["SYMBOL"]).strip()

        company = str(row["NAME OF COMPANY"]).strip()

        isin = str(row[" ISIN NUMBER"]).strip()

        stock = (
            db.query(Stock)
            .filter(Stock.symbol == symbol)
            .first()
        )

        if stock:

            stock.company_name = company
            stock.isin = isin

            updated += 1

        else:

            db.add(
                Stock(
                    symbol=symbol,
                    company_name=company,
                    exchange="NSE",
                    isin=isin
                )
            )

            added += 1

    db.commit()

    return {
        "added": added,
        "updated": updated
    }
