from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.price_service import download_history

router = APIRouter(
    prefix="/prices",
    tags=["Prices"]
)


@router.post("/{symbol}")
def download_stock_price(
    symbol: str,
    db: Session = Depends(get_db)
):

    return download_history(
        symbol.upper(),
        db
    )
