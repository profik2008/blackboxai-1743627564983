from news.scrapers.i24news_scraper import I24NewsScraper
import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from news.scrapers.utils import RequestHandler

def format_article(article):
    """Format article data for display"""
    if not article:
        return "Failed to scrape article"
        
    # Convert datetime to string if present
    if article.get('pub_date') and isinstance(article['pub_date'], datetime):
        article['pub_date'] =
def main():
    scraper = I24NewsScraper()
    
    # Example article URL - using a real article from i24news
    url = "https://www.i24news.tv/en/news/israel"
    
    print(f"\nScraping article from: {url}\n")
    
    # Scrape the article
    article = scraper.scrape_article(url)
    
    # Display results
    print("Scraping Results:")
    print("=" * 50)
    print(format_article(article))

if __name__ == "__main__":
    main()