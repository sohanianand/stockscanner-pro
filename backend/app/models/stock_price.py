from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import BigInteger
from sqlalchemy import Date

from app.database.database import Base


class StockPrice(Base):

    __tablename__ = "stock_prices"

    id = Column(Integer, primary_key=True, index=True)

    symbol = Column(String(30), index=True, nullable=False)

    trading_date = Column(Date, index=True, nullable=False)

    open = Column(Float)

    high = Column(Float)

    low = Column(Float)

    close = Column(Float)

    adj_close = Column(Float)

    volume = Column(BigInteger)
