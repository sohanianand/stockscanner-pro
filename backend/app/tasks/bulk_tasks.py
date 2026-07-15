from app.tasks.celery_app import celery

from app.database.database import SessionLocal

from app.models.stock import Stock

from app.tasks.full_refresh import refresh_stock


@celery.task
def refresh_all_stocks():

    db = SessionLocal()

    try:

        stocks = db.query(Stock).all()

        total = len(stocks)

        for stock in stocks:

            refresh_stock.delay(
                stock.symbol
            )

        return {
            "submitted": total
        }

    finally:

        db.close()
