from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.alert import AlertCreate
from app.services.alert_service import AlertService

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


# Replace with your JWT dependency
def get_current_user():
    return {"id": 1}


@router.post("")
def create_alert(
    request: AlertCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):

    service = AlertService(db)

    return service.create(
        user["id"],
        request,
    )
