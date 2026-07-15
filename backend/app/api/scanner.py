from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.scanner import ScanRequest

from app.services.scanner_service import run_scan

router = APIRouter(
    prefix="/scanner",
    tags=["Scanner"]
)


@router.post("/run")
def scanner(
    request: ScanRequest,
    db: Session = Depends(get_db)
):
    return run_scan(
        request.filters,
        db
    )
