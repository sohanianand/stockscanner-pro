from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date

from app.database.database import Base


class Indicator(Base):

    __tablename__ = "indicators"

    id = Column(Integer, primary_key=True, index=True)

    symbol = Column(String(30), index=True)

    trading_date = Column(Date, index=True)

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
