from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TradeBase(BaseModel):
    pair: str
    direction: str
    entry_price: float
    exit_price: float
    stop_loss: float
    take_profit: float
    emotion: Optional[str] = None
    notes: Optional[str] = None
    screenshot_url: Optional[str] = None


class TradeCreate(TradeBase):
    pass


class TradeResponse(TradeBase):
    id: int
    user_id: int
    pnl: Optional[float]
    created_at: datetime

    class Config:
        from_attributes = True
