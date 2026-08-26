import requests
import feedparser
from newspaper import Article


def news_collector(url_dict: dict) -> list[dict]:
    """Collect recent financial headlines and article text from RSS sources."""
    headers = {"User-Agent": "Mozilla/5.0"}
    news_data = []

    for source, url in url_dict.items():
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            feed = feedparser.parse(response.content)

            for entry in feed.entries[:10]:
                article_info = {
                    "source": source,
                    "title": entry.get("title", ""),
                    "url": entry.get("link", ""),
                    "published": entry.get("published", ""),
                }

                try:
                    article = Article(article_info["url"])
                    article.download()
                    article.parse()
                    article_info["content"] = article.text.strip()
                except Exception:
                    article_info["content"] = "Article content unavailable."

                news_data.append(article_info)
        except Exception:
            continue

    return news_data
