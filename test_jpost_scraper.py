from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal_project.settings')
setup()

from news.scrapers.jpost_scraper import JPostScraper
import requests
from bs4 import BeautifulSoup

def test_specific_article():
    scraper = JPostScraper()
    url = "https://www.jpost.com/israel-news/article-848606"
    
    print("Testing article scraping...")
    
    try:
        response = requests.get(url, headers=scraper.headers)
        print("\nURL Status Code:", response.status_code)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            
            print("\nSearching for article elements...")
            
            # Find the article title
            title = soup.find('h1', class_='article-title')
            if title:
                print("\nTitle:", title.get_text().strip())
            
            # Find the article subtitle
            subtitle = soup.find('h2', class_='article-subtitle')
            if subtitle:
                print("\nSubtitle:", subtitle.get_text().strip())
            
            # Find all divs with class containing 'article'
            print("\nSearching for article content divs...")
            for div in soup.find_all('div', class_=lambda x: x and 'article' in x.lower()):
                print("\nFound div with classes:", div.get('class', []))
                
                # Look for paragraphs in this div
                paragraphs = div.find_all('p')
                if paragraphs:
                    print(f"Found {len(paragraphs)} paragraphs. First paragraph:")
                    print(paragraphs[0].get_text().strip())
            
            # Try the scraper
            print("\nTrying scraper...")
            article = scraper.scrape_article(url)
            
            if article:
                print("\nScraper results:")
                print("Title:", article.title)
                paragraphs = article.content.split('\n\n')
                print("\nContent (%d paragraphs):" % len(paragraphs))
                for i, para in enumerate(paragraphs, 1):
                    print("\nParagraph %d:" % i)
                    print(para)
            else:
                print("Scraper failed to create article")
                
        else:
            print("Failed to access URL. Status code:", response.status_code)
            
    except Exception as e:
        print("Error during testing:", str(e))

if __name__ == "__main__":
    test_specific_article()