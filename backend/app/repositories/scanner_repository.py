from sqlalchemy import and_
from sqlalchemy import or_

from app.models.latest_indicator import LatestIndicator


class ScannerRepository:

    def __init__(self, db):

        self.db = db

    def scan(
        self,
        expressions,
        use_or=False,
    ):

        query = self.db.query(LatestIndicator)

        if expressions:

            if use_or:

                query = query.filter(
                    or_(*expressions)
                )

            else:

                query = query.filter(
                    and_(*expressions)
                )

        return query
