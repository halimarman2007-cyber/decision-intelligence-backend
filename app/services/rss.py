import feedparser
from urllib.parse import quote_plus

def fetch_rss(query: str, limit: int = 20):
    # ✅ Encode query safely for URLs
    encoded_query = quote_plus(query)

    url = f"https://news.google.com/rss/search?q={encoded_query}"
    feed = feedparser.parse(url)

    items = []
    for entry in feed.entries[:limit]:
        text = f"{entry.title} {entry.get('summary', '')}"
        items.append({
            "text": text,
            "source": "Google News",
            "published": entry.get("published", ""),
        })

    return items
