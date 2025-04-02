import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal_project.settings')
django.setup()

from news.scrapers.jpost_scraper import JPostScraper

def test_jpost_scraper():
    scraper = JPostScraper()
    print("Testing JPost scraper...")
    
    # Test fetching article URLs
    print("\nFetching article URLs...")
    urls = scraper.fetch_article_urls(limit=5)
    print(f"Found {len(urls)} article URLs:")
    for url in urls:
        print(f"- {url}")
    
    if not urls:
        print("Error: No article URLs found")
        return
    
    # Test scraping a single article
    print("\nTesting article scraping...")
    test_url = urls[0]
    print(f"Scraping article from: {test_url}")
    
    article = scraper.scrape_article(test_url)
    if article:
        print("\nArticle successfully scraped:")
        print(f"Title: {article.title}")
        print(f"Source: {article.source}")
        print(f"Language: {article.original_language}")
        print(f"Publication date: {article.publication_date}")
        print(f"Content preview: {article.content[:200]}...")
    else:
        print("Error: Failed to scrape article")

if __name__ == "__main__":
    test_jpost_scraper()