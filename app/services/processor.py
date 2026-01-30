from app.services.rss import fetch_rss
from app.services.hackernews import fetch_hn
from app.rules import analyze_text
from app.database import SessionLocal
from app.models import MarketSnapshot

def process_market(market: str, query: str):
    rss_items = fetch_rss(query)
    hn_items = fetch_hn(limit=10)

    texts = [item["text"] for item in rss_items + hn_items]
    

# -----------------------------------------------------

    trend, strength, confidence, insights, risks, alerts = analyze_text(texts)

    db = SessionLocal()

    previous = (
        db.query(MarketSnapshot)
        .filter(MarketSnapshot.market == market)
        .order_by(MarketSnapshot.created_at.desc())
        .first()
    )

    momentum = "flat"
    if previous:
        if confidence > previous.confidence + 2:
            momentum = "improving"
        elif confidence < previous.confidence - 2:
            momentum = "weakening"
        if previous.trend != trend:
            alerts.append(f"Trend reversal: {previous.trend} → {trend}")

    snapshot = MarketSnapshot(
        market=market,
        trend=trend,
        confidence=confidence,
        momentum=momentum,
        rationale=f"{strength.capitalize()} sentiment ({confidence}% confidence, {momentum})",
        insights="; ".join(insights),
        risks="; ".join(risks),
        alerts="; ".join(alerts),
    )

    db.add(snapshot)
    db.commit()
    db.close()
