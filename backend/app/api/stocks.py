from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.stock import Stock

from app.schemas.stock import StockResponse

from app.services.nse_import import import_nse_stocks

router = APIRouter(
    prefix="/stocks",
    tags=["Stocks"]
)


@router.get(
    "",
    response_model=list[StockResponse]
)
def get_all_stocks(
    db: Session = Depends(get_db)
):

    return db.query(Stock).order_by(
        Stock.symbol
    ).all()

@router.post("/import")
def import_all_stocks(
    db: Session = Depends(get_db)
):
    return import_nse_stocks(db)
