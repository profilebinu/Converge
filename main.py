import requests
from bs4 import BeautifulSoup

# URL of The Verge's RSS feed
RSS_FEED_URL = "https://www.theverge.com/rss/index.xml"

def fetch_news():
    """
    Fetches and displays the latest news from The Verge.
    """
    try:
        # Step 1: Fetch the RSS feed
        response = requests.get(RSS_FEED_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Step 2: Parse the RSS feed with BeautifulSoup
        soup = BeautifulSoup(response.content, 'xml')

        # Step 3: Find all items (articles) in the RSS feed
        articles = soup.find_all('item')

        # Step 4: Iterate through articles and display the information
        for idx, article in enumerate(articles[:10]):  # Limiting to 10 articles for brevity
            title = article.title.text
            description = article.description.text
            # Extract the image URL from the content or media tag
            image = article.find('media:thumbnail') or article.find('media:content')
            image_url = image['url'] if image else "No image available"

            # Print article details to the console
            print(f"Article {idx + 1}")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"Image URL: {image_url}")
            print("-" * 80)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_news()

