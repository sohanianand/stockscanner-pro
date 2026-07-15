from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.latest_indicator_service import update_latest

router = APIRouter(
    prefix="/latest",
    tags=["Latest Indicators"]
)


@router.post("/{symbol}")
def latest_indicator(
    symbol: str,
    db: Session = Depends(get_db)
):
    return update_latest(
        symbol.upper(),
        db
    )
