from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.backtest import BacktestRequest

from app.services.backtest_service import BacktestService

router = APIRouter(
    prefix="/backtest",
    tags=["Backtest"],
)


@router.post("")
def run_backtest(
    request: BacktestRequest,
    db: Session = Depends(get_db),
):

    service = BacktestService(db)

    return service.run(request)
