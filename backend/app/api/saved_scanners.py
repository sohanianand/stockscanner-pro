from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.saved_scanner import (
    SavedScannerCreate,
    SavedScannerResponse,
)
from app.services.saved_scanner_service import SavedScannerService

router = APIRouter(
    prefix="/saved-scanners",
    tags=["Saved Scanners"],
)


# Replace this with your JWT current-user dependency
def get_current_user():
    return {"id": 1}


@router.post("", response_model=SavedScannerResponse)
def create_scanner(
    request: SavedScannerCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    service = SavedScannerService(db)

    return service.create(user["id"], request)


@router.get("", response_model=list[SavedScannerResponse])
def list_scanners(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    service = SavedScannerService(db)

    return service.list(user["id"])


@router.delete("/{scanner_id}")
def delete_scanner(
    scanner_id: int,
    db: Session = Depends(get_db),
):
    service = SavedScannerService(db)

    deleted = service.delete(scanner_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Scanner not found",
        )

    return {"message": "Scanner deleted"}
