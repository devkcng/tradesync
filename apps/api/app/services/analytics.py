from sqlalchemy.orm import Session
from ..models import Trade


def calculate_stats(user_id: int, db: Session):
    trades = db.query(Trade).filter(Trade.user_id == user_id).all()

    if not trades:
        return {"win_rate": 0, "profit_factor": 0}

    wins = [t for t in trades if t.pnl > 0]
    losses = [t for t in trades if t.pnl <= 0]

    win_rate = (len(wins) / len(trades)) * 100

    gross_profit = sum(t.pnl for t in wins)
    gross_loss = abs(sum(t.pnl for t in losses))

    profit_factor = gross_profit / gross_loss if gross_loss > 0 else 999.0

    return {
        "total_trades": len(trades),
        "win_rate": round(win_rate, 2),
        "profit_factor": round(profit_factor, 2),
        "gross_profit": gross_profit
    }
