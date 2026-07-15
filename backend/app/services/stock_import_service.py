import csv

from sqlalchemy.orm import Session

from app.models.stock import Stock


def import_stocks(
    db: Session,
    csv_file: str
):

    with open(
        csv_file,
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            exists = db.query(
                Stock
            ).filter(
                Stock.symbol == row["symbol"]
            ).first()

            if exists:
                continue

            stock = Stock(

                symbol=row["symbol"],

                company_name=row["company_name"],

                exchange=row.get(
                    "exchange",
                    "NSE"
                ),

                sector=row.get(
                    "sector"
                ),

                industry=row.get(
                    "industry"
                ),

                isin=row.get(
                    "isin"
                )
            )

            db.add(stock)

        db.commit()
