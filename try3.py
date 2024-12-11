import feedparser
import logging
from typing import List, Dict
from tabulate import tabulate

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
            image_url = entry.media_content[0]['url'] if 'media_content' in entry else "No image available"

            news_item = {
                "Title": title,
                "Description": description,
                "Image URL": image_url
            }
            news_list.append(news_item)

            # Log article details
            logging.info(f"Article {idx + 1}: {title}")

        return news_list

    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return []

def display_news(news: List[Dict[str, str]], save_to_file: bool = False):
    """
    Displays the news in a tabular format and optionally saves it to a file.
    """
    table = [[idx + 1, article['Title'], article['Description'], article['Image URL']] for idx, article in enumerate(news)]
    table_str = tabulate(table, headers=["#", "Title", "Description", "Image URL"], tablefmt="grid")
    print(table_str)

    if save_to_file:
        with open("news_output.txt", "w", encoding="utf-8") as file:
            file.write(table_str)

if __name__ == "__main__":
    news = fetch_news()
    if news:
        display_news(news, save_to_file=True)  # Change to False if you don't want to save to a file
    else:
        print("No news articles found.")
