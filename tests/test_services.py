from services.rss_feed import fetch_techcrunch_articles

def test_rss_feed():
    articles = fetch_techcrunch_articles()
    assert len(articles) > 0, "No articles fetched!"

if __name__ == "__main__":
    test_rss_feed()