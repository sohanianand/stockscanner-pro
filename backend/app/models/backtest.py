from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func

from app.database.database import Base


class Backtest(Base):

    __tablename__ = "backtests"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    scanner_id = Column(
        Integer,
        ForeignKey("saved_scanners.id"),
        nullable=False
    )

    start_date = Column(Date)

    end_date = Column(Date)

    total_signals = Column(Integer)

    winners = Column(Integer)

    losers = Column(Integer)

    win_rate = Column(Float)

    average_return = Column(Float)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
