import requests

HEADERS = {
    "User-Agent": "decision-intelligence/0.1"
}

def fetch_posts(subreddit: str, limit: int = 30):
    url = f"https://www.reddit.com/r/{subreddit}/new.json?limit={limit}"
    response = requests.get(url, headers=HEADERS, timeout=10)

    if response.status_code != 200:
        return []

    data = response.json()
    posts = []

    for item in data.get("data", {}).get("children", []):
        post = item["data"]
        title = post.get("title", "")
        body = post.get("selftext", "")
        posts.append(f"{title} {body}")

    return posts
