from fastapi import APIRouter

from app.tasks.bulk_tasks import refresh_all_stocks
from app.tasks.full_refresh import refresh_stock
from app.tasks.celery_app import celery


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"])

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"])



@router.post("/refresh/{symbol}")
def refresh_one(symbol: str):

    task = refresh_stock.delay(
        symbol.upper()
    )

    return {
        "task_id": task.id,
        "symbol": symbol.upper(),
        "status": "submitted"
    }


@router.post("/refresh-all")
def refresh_all():

    task = refresh_all_stocks.delay()

    return {
        "task_id": task.id,
        "status": "submitted"
    }

@router.get("/{task_id}")
def task_status(task_id: str):
    task = AsyncResult(task_id, app=celery)

    return {
        "task_id": task.id,
        "status": task.status,
        "result": task.result if task.ready() else None,
    }
