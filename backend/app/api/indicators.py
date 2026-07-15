from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.indicator_service import calculate_indicators

router = APIRouter(
    prefix="/indicators",
    tags=["Indicators"]
)


@router.post("/{symbol}")
def generate_indicators(
    symbol: str,
    db: Session = Depends(get_db)
):
    return calculate_indicators(
        symbol.upper(),
        db
    )
