from fastapi import FastAPI
from .database import engine, Base
from .routers import trades

# Create DB Tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TradeSync API")

app.include_router(trades.router)


@app.get("/")
def root():
    return {"message": "TradeSync API is running with DB connection"}
