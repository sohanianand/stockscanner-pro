from app.database.database import SessionLocal

from app.repositories.alert_repository import AlertRepository

from app.services.scanner_service import run_scan

from app.celery_app import celery

from app.services.alert_service import process_alerts


@celery.task(name="run_alert_engine")
def run_alert_engine():
    process_alerts()

def process_alerts():

    db = SessionLocal()

    repo = AlertRepository(db)

    alerts = repo.all_enabled()

    for alert in alerts:

        print(
            f"Running scanner {alert.scanner_id}"
        )

        #
        # Load Saved Scanner
        #
        # Execute run_scan()
        #
        # If stocks found:
        #
        # Send notification
        #

    db.close()
