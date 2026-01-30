from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class MarketSnapshot(Base):
    __tablename__ = "market_snapshots"

    id = Column(Integer, primary_key=True)
    market = Column(String, nullable=False)

    trend = Column(String, nullable=False)
    confidence = Column(Integer, nullable=False)
    momentum = Column(String, nullable=False)

    rationale = Column(Text)
    insights = Column(Text)
    risks = Column(Text)
    alerts = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
