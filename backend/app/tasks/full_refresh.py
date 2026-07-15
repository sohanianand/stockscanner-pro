from app.tasks.celery_app import celery

from app.database.database import SessionLocal

from app.services.price_service import download_history
from app.services.indicator_service import calculate_indicators
from app.services.latest_indicator_service import update_latest


@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
def refresh_stock(self, symbol: str):
    db = SessionLocal()

    try:
        symbol = symbol.upper()

        download_history(symbol, db)
        calculate_indicators(symbol, db)
        update_latest(symbol, db)

        return {
            "symbol": symbol,
            "status": "completed"
        }

    finally:
        db.close()
