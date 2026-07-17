from celery import Celery
from celery.schedules import crontab

celery = Celery(
    "stockscanner",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

celery.conf.update(
    timezone="Asia/Kolkata",
    enable_utc=True,
)

# Schedule Celery Beat tasks
celery.conf.beat_schedule = {
    "scanner-alerts": {
        "task": "run_alert_engine",
        "schedule": crontab(
            minute="*/15"
        ),
    },
}

# Discover all tasks
celery.autodiscover_tasks(["app.tasks"])
