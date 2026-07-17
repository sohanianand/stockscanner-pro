from datetime import datetime
from typing import Any

from pydantic import BaseModel


class SavedScannerCreate(BaseModel):
    name: str
    description: str | None = None
    definition: dict[str, Any]


class SavedScannerUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    definition: dict[str, Any] | None = None


class SavedScannerResponse(BaseModel):
    id: int
    user_id: int
    name: str
    description: str | None
    definition: dict[str, Any]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
