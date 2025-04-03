import requests
from bs4 import BeautifulSoup
import json

def check_website():
    url = "https://www.i24news.tv/en/news/israel"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        print("\nPage Structure Analysis:")
        print("=" * 50)
        
        # Check title element
        title = soup.find('title')
        print(f"\nTitle tag: {title.text if title else 'Not found'}")
        
        # Check meta tags
        meta_tags = soup.find_all('meta')
        print("\nMeta tags:")
        for meta in meta_tags[:5]:  # Show first 5 meta tags
            print(f"- {meta}")
            
        # Check main content structure
        print("\nMain content containers:")
        containers = soup.find_all(['div', 'article'], class_=True)
        for container in containers[:5]:  # Show first 5 containers
            print(f"- {container.name}: {container.get('class')}")
            
        # Look for article links
        print("\nArticle links:")
        article_links = soup.find_all('a', href=True)
        for link in article_links[:5]:  # Show first 5 links
            if '/news/' in link['href']:
                print(f"- {link['href']}: {link.text.strip()}")
                
    except Exception as e:
        print(f"Error accessing website: {str(e)}")

if __name__ == "__main__":
    check_website()