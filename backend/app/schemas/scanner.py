from enum import Enum
from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel


class Operator(str, Enum):
    eq = "="
    gt = ">"
    lt = "<"
    gte = ">="
    lte = "<="
    ne = "!="


class LogicalOperator(str, Enum):
    AND = "AND"
    OR = "OR"


class SortDirection(str, Enum):
    asc = "asc"
    desc = "desc"


class ScannerFilter(BaseModel):

    field: str

    operator: Operator

    value: Union[float, int, str]


class SortRequest(BaseModel):

    field: str

    direction: SortDirection = SortDirection.desc


class ScannerRequest(BaseModel):

    condition: LogicalOperator = LogicalOperator.AND

    filters: List[ScannerFilter]

    sort: Optional[SortRequest] = None

    page: int = 1

    page_size: int = 50
