import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal_project.settings')
django.setup()

from news.scrapers.jpost_scraper import JPostScraper
from news.models import Article

def test_jpost_scraper():
    scraper = JPostScraper()
    print("Testing JPost scraper...")
    
    # Test fetching and saving articles
    print("\nFetching and saving articles...")
    articles = scraper.scrape_latest_articles(limit=3, force=True)  # Reduced to 3 for clearer output
    print(f"\nSaved {len(articles)} articles to database:")
    for article in articles:
        print(f"\n- Title: {article.title}")
        print(f"  URL: {article.url}")
        print(f"  Source: {article.source}")
        print(f"  Language: {article.original_language}")
        print(f"  Publication date: {article.publication_date}")
        print(f"  Content preview: {article.content[:200]}...")
    
    # Verify articles in database
    db_articles = Article.objects.all()
    print(f"\nTotal articles in database: {db_articles.count()}")

if __name__ == "__main__":
    # Clean up existing test articles
    Article.objects.all().delete()
    print("Cleaned up existing articles")
    
    # Run the test
    test_jpost_scraper()