import requests

HN_TOP = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def fetch_hn(limit=20):
    ids = requests.get(HN_TOP, timeout=10).json()[:limit]
    items = []

    for i in ids:
        data = requests.get(HN_ITEM.format(i), timeout=10).json()
        if not data:
            continue
        title = data.get("title", "")
        items.append({
            "text": title,
            "source": "Hacker News",
            "published": data.get("time"),
        })

    return items
