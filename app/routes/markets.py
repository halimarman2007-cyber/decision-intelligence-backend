from fastapi import APIRouter
from app.database import SessionLocal
from app.models import MarketSnapshot

router = APIRouter()

@router.get("/markets")
def get_markets():
    db = SessionLocal()

    snapshot = (
        db.query(MarketSnapshot)
        .order_by(MarketSnapshot.created_at.desc())
        .first()
    )

    db.close()

    if not snapshot:
        return []

    return [
        {
            "id": snapshot.id,
            "name": snapshot.market,
            "symbol": snapshot.market.upper(),
            "trendDirection": snapshot.trend,
            "trendRationale": snapshot.rationale,
            "confidence": snapshot.confidence,
            "momentum": snapshot.momentum,
            "insights": snapshot.insights.split("; ") if snapshot.insights else [],
            "riskSignals": snapshot.risks.split("; ") if snapshot.risks else [],
            "alerts": snapshot.alerts.split("; ") if snapshot.alerts else [],
        }
    ]
