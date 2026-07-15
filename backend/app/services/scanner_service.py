from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models.latest_indicator import LatestIndicator


FIELD_MAP = {
    "close": LatestIndicator.close,
    "ema20": LatestIndicator.ema20,
    "ema50": LatestIndicator.ema50,
    "sma20": LatestIndicator.sma20,
    "rsi": LatestIndicator.rsi,
    "macd": LatestIndicator.macd,
    "macd_signal": LatestIndicator.macd_signal,
}


def run_scan(filters, db: Session):

    query = db.query(LatestIndicator)

    conditions = []

    for f in filters:

        if f.field not in FIELD_MAP:
            continue

        left = FIELD_MAP[f.field]

        if isinstance(f.value, str) and f.value in FIELD_MAP:
            right = FIELD_MAP[f.value]
        else:
            right = f.value

        if f.operator == ">":
            conditions.append(left > right)

        elif f.operator == "<":
            conditions.append(left < right)

        elif f.operator == "=":
            conditions.append(left == right)

        elif f.operator == ">=":
            conditions.append(left >= right)

        elif f.operator == "<=":
            conditions.append(left <= right)

        elif f.operator == "!=":
            conditions.append(left != right)

    if conditions:
        query = query.filter(and_(*conditions))

    return query.all()
