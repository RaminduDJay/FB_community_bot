import feedparser

def fetch_techcrunch_articles(n=5):
    feed = feedparser.parse("https://techcrunch.com/feed/") 
    return [{
        "title": entry.title,
        "summary": entry.summary,
        "link": entry.link
    } for entry in feed.entries[:n]]