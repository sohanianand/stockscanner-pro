from sqlalchemy import asc
from sqlalchemy import desc

from app.models.latest_indicator import LatestIndicator
from app.repositories.scanner_repository import ScannerRepository
from app.core.scanner_fields import SCANNER_FIELDS

OPERATORS = {
    "=": lambda c, v: c == v,
    ">": lambda c, v: c > v,
    "<": lambda c, v: c < v,
    ">=": lambda c, v: c >= v,
    "<=": lambda c, v: c <= v,
    "!=": lambda c, v: c != v,
}


def run_scan(request, db):

    repo = ScannerRepository(db)

    expressions = []

    for f in request.filters:

        if not hasattr(LatestIndicator, f.field):

            raise ValueError(
                f"Unknown field: {f.field}"
            )

        column = SCANNER_FIELDS.get(f.field)

        if column is None:

           raise ValueError(
                f"Unknown scanner field {f.field}"
           ) 

        expressions.append(
            OPERATORS[f.operator.value](
                column,
                f.value,
            )
        )

    query = repo.scan(
        expressions,
        use_or=request.condition.value == "OR",
    )

    if request.sort:

        column = getattr(
            LatestIndicator,
            request.sort.field,
        )

        if request.sort.direction.value == "asc":

            query = query.order_by(
                asc(column)
            )

        else:

            query = query.order_by(
                desc(column)
            )

    total = query.count()

    rows = (
        query.offset(
            (request.page - 1)
            * request.page_size
        )
        .limit(
            request.page_size
        )
        .all()
    )

    return {

        "total": total,

        "page": request.page,

        "page_size": request.page_size,

        "results": rows,
    }
