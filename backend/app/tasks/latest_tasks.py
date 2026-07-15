from app.tasks.celery_app import celery

from app.database.database import SessionLocal

from app.services.latest_indicator_service import update_latest


@celery.task(name="update_latest_indicator")
def update_latest_indicator(symbol: str):

    db = SessionLocal()

    try:

        result = update_latest(
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
