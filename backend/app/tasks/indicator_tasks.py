from app.tasks.celery_app import celery

from app.database.database import SessionLocal

from app.services.indicator_service import calculate_indicators


@celery.task(name="calculate_stock_indicator")
def calculate_stock_indicator(symbol: str):

    db = SessionLocal()

    try:

        result = calculate_indicators(
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
