from fastapi import FastAPI

from app.database.init_db import init_database

from app.api.auth import router as auth_router

from app.api.stocks import router as stock_router

from app.api.prices import router as prices_router

from app.api.indicators import router as indicator_router

from app.api.scanner import router as scanner_router

from app.api.latest_indicator import router as latest_router

from app.api.tasks import router as task_router

from app.api.saved_scanners import router as saved_scanner_router

from app.api.backtest import router as backtest_router

app = FastAPI(
    title="StockScanner Pro"
)

app.include_router(auth_router)
app.include_router(stock_router)
app.include_router(prices_router)
app.include_router(indicator_router)
app.include_router(scanner_router)
app.include_router(latest_router)
app.include_router(task_router)
app.include_router(saved_scanner_router)
app.include_router(backtest_router)


@app.get("/")
def root(): 
    return {
        "application": "StockScanner Pro"
    }


@app.on_event("startup")
def startup():

    init_database()

    print("Database Initialized")


@app.get("/")
def home():

    return {
        "message": "StockScanner Pro API Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }
