from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    trades = relationship("Trade", back_populates="owner")


class Trade(Base):
    __tablename__ = "trades"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    pair = Column(String)  # e.g., "EURUSD"
    direction = Column(String)  # "LONG" or "SHORT"
    entry_price = Column(Float)
    exit_price = Column(Float)
    stop_loss = Column(Float)
    take_profit = Column(Float)
    pnl = Column(Float, nullable=True)  # Profit/Loss

    emotion = Column(String, nullable=True)  # "FOMO", "Calm", etc.
    notes = Column(Text, nullable=True)
    screenshot_url = Column(String, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="trades")
