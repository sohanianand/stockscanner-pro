from typing import Union

from pydantic import BaseModel


class ScanFilter(BaseModel):
    field: str
    operator: str
    value: Union[float, str]


class ScanRequest(BaseModel):
    filters: list[ScanFilter]
