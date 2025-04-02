from django import setup
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal_project.settings')
setup()

from news.models import Article

articles = Article.objects.all().order_by('-publication_date')
for article in articles:
    print(f"\nID: {article.id}")
    print(f"Title: {article.title}")
    print(f"URL: {article.url}")
    print("-" * 80)