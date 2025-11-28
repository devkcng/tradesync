from fastapi import FastAPI

app = FastAPI(title="TradeSync API")

@app.get("/")
def root():
    return {"message": "TradeSync API running"}
