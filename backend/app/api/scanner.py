from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.scanner import ScannerRequest

from app.services.scanner_service import run_scan

router = APIRouter(
    prefix="/scanner",
    tags=["Scanner"]
)


@router.post("/run")
def scanner(
    request: ScannerRequest,
    db: Session = Depends(get_db)
):
    return run_scan(
        request.filters,
        db
    )

@router.post("/scan")
def scan(
    request: ScannerRequest,
    db: Session = Depends(get_db),
):

    return run_scan(
        request,
        db,
    )
