from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date

from app.database.database import Base


class LatestIndicator(Base):

    __tablename__ = "latest_indicators"

    id = Column(Integer, primary_key=True, index=True)

    symbol = Column(
        String(30),
        unique=True,
        index=True,
        nullable=False
    )

    trading_date = Column(Date)

    close = Column(Float)

    ema20 = Column(Float)
    ema50 = Column(Float)
    sma20 = Column(Float)

    rsi = Column(Float)

    macd = Column(Float)
    macd_signal = Column(Float)
    macd_histogram = Column(Float)

    bb_upper = Column(Float)
    bb_middle = Column(Float)
    bb_lower = Column(Float)

    volume = Column(Float)
