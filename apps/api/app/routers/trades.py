from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/trades", tags=["trades"])


@router.post("/", response_model=schemas.TradeResponse)
def create_trade(trade: schemas.TradeCreate, db: Session = Depends(get_db)):
    # Simple PnL Calc (Logic can be moved to a service later)
    calculated_pnl = 0.0
    if trade.direction == "LONG":
        calculated_pnl = (trade.exit_price - trade.entry_price)
    else:
        calculated_pnl = (trade.entry_price - trade.exit_price)

    # In a real app, you'd get user_id from the JWT token
    fake_user_id = 1

    db_trade = models.Trade(
        **trade.dict(), pnl=calculated_pnl, user_id=fake_user_id)
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade


@router.get("/", response_model=List[schemas.TradeResponse])
def read_trades(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    trades = db.query(models.Trade).offset(skip).limit(limit).all()
    return trades
