from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.database import Base


class Stock(Base):

    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True)

    symbol = Column(String(30), unique=True, nullable=False)

    company_name = Column(String(255))

    exchange = Column(String(20))

    sector = Column(String(100))

    industry = Column(String(100))

    isin = Column(String(30))
