
# -------------------------------
# Keyword dictionaries (rule-based)
# -------------------------------

POSITIVE = [
    "growth", "bullish", "adoption", "surge", "record", "expansion",
    "increase", "strong", "positive", "uptrend", "profit", "demand"
]

NEGATIVE = [
    "decline", "bearish", "drop", "risk", "weak", "loss",
    "regulation", "lawsuit", "crash", "slowdown", "concern"
]

RISK = [
    "risk", "regulation", "ban", "lawsuit", "hack",
    "uncertainty", "volatility", "investigation"
]

def analyze_text(posts):
    text = " ".join(posts).lower()

    pos = sum(text.count(word) for word in POSITIVE)
    neg = sum(text.count(word) for word in NEGATIVE)
    total_mentions = pos + neg

    sentiment_ratio = pos / (total_mentions + 1)

    if sentiment_ratio > 0.6:
        trend = "bullish"
    elif sentiment_ratio < 0.4:
        trend = "bearish"
    else:
        trend = "neutral"

    if total_mentions > 15:
        strength = "strong"
    elif total_mentions > 7:
        strength = "moderate"
    else:
        strength = "weak"

    confidence = int(sentiment_ratio * 100)

    insights = []

    # 1️⃣ Sentiment imbalance
    if pos >= 2 and pos > neg * 2:
        insights.append(
            "Positive sentiment materially outweighs negative discussion"
        )

    if neg >= 2 and neg > pos:
        insights.append(
            "Negative narratives are becoming more prominent"
        )

    # 2️⃣ Volume spike / drought
    if total_mentions >= 10:
        insights.append(
            "Unusually high discussion volume suggests rising attention"
        )

    if total_mentions <= 2:
        insights.append(
            "Low discussion volume indicates weak or uncertain signal"
        )

    # 3️⃣ Confidence-quality insight
    if total_mentions < 3:
        insights.append(
            "Signal confidence is low due to limited data points"
        )


    risks = []
    alerts = []

    if neg > pos:
        alerts.append("Negative sentiment outweighs positive mentions")

    if total_mentions < 3:
        alerts.append("Low signal volume — confidence may be unreliable")

    return trend, strength, confidence, insights, risks, alerts
