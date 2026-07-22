from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    title="StockScanner Pro",
    version="1.0.0"
)


# --------------------------------------------------
# CORS CONFIGURATION
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://192.168.0.106:5173",
        "http://192.168.0.108:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# API ROUTES
# --------------------------------------------------

app.include_router(auth_router)
app.include_router(stock_router)
app.include_router(prices_router)
app.include_router(indicator_router)
app.include_router(scanner_router)
app.include_router(latest_router)
app.include_router(task_router)
app.include_router(saved_scanner_router)
app.include_router(backtest_router)


# --------------------------------------------------
# ROOT ENDPOINT
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "application": "StockScanner Pro",
        "message": "StockScanner Pro API Running"
    }


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# --------------------------------------------------
# DATABASE INITIALIZATION
# --------------------------------------------------

@app.on_event("startup")
def startup():
    init_database()
    print("Database Initialized")
