import feedparser
import logging
from typing import List, Dict

# URL of The Verge's RSS feed
RSS_FEED_URL = "https://www.theverge.com/rss/index.xml"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_news() -> List[Dict[str, str]]:
    """
    Fetches and returns the latest news from The Verge.
    """
    try:
        # Step 1: Fetch the RSS feed
        feed = feedparser.parse(RSS_FEED_URL)

        news_list = []

        # Step 2: Iterate through entries and collect the information
        for idx, entry in enumerate(feed.entries[:10]):  # Limiting to 10 articles for brevity
            title = entry.title if 'title' in entry else "No title available"
            description = entry.description if 'description' in entry else "No description available"
            # Extract the image URL from the content or media tag
            image_url = entry.media_thumbnail[0]['url'] if 'media_thumbnail' in entry else "No image available"

            news_item = {
                "title": title,
                "description": description,
                "image_url": image_url
            }
            news_list.append(news_item)

            # Log article details
            logging.info(f"Article {idx + 1}: {title}")

        return news_list

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return []

if __name__ == "__main__":
    news = fetch_news()
    if news:
        for idx, article in enumerate(news):
            print(f"Article {idx + 1}")
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"Image URL: {article['image_url']}")
            print("-" * 80)
    else:
        print("No news articles found.")