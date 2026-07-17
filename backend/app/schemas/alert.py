from pydantic import BaseModel


class AlertCreate(BaseModel):

    scanner_id: int

    notification_type: str = "email"


class AlertResponse(BaseModel):

    id: int

    scanner_id: int

    notification_type: str

    enabled: bool

    class Config:
        from_attributes = True
