from app.tasks.celery_app import celery

from app.database.database import SessionLocal

from app.services.price_service import download_history


@celery.task(name="download_stock_price")
def download_stock_price(symbol: str):

    db = SessionLocal()

    try:

        result = download_history(
            symbol.upper(),
            db
        )

        return result

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }

    finally:

        db.close()
