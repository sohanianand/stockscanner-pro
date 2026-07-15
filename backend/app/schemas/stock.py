from pydantic import BaseModel


class StockResponse(BaseModel):
    id: int
    symbol: str

    company_name: str | None = None
    exchange: str | None = None
    sector: str | None = None
    industry: str | None = None
    isin: str | None = None

    class Config:
        from_attributes = True
