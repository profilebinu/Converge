import requests
from bs4 import BeautifulSoup
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
        response = requests.get(RSS_FEED_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Step 2: Parse the RSS feed with BeautifulSoup
        soup = BeautifulSoup(response.content, 'xml')

        # Step 3: Find all items (articles) in the RSS feed
        articles = soup.find_all('item')

        news_list = []

        # Step 4: Iterate through articles and collect the information
        for idx, article in enumerate(articles[:10]):  # Limiting to 10 articles for brevity
            title = article.title.text if article.title else "No title available"
            description = article.description.text if article.description else "No description available"
            # Extract the image URL from the content or media tag
            image = article.find('media:thumbnail') or article.find('media:content')
            image_url = image['url'] if image else "No image available"

            news_item = {
                "title": title,
                "description": description,
                "image_url": image_url
            }
            news_list.append(news_item)

            # Log article details
            logging.info(f"Article {idx + 1}: {title}")

        return news_list

    except requests.RequestException as e:
        logging.error(f"HTTP error occurred: {e}")
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