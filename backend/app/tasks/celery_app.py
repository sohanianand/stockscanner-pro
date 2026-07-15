from celery import Celery
from app.core.config import settings

celery = Celery(
    "stockscanner",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

celery.conf.update(
    timezone="Asia/Kolkata",
    enable_utc=False,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    result_expires=3600,
)

celery.autodiscover_tasks(
    [
        "app.tasks"
    ]
)
