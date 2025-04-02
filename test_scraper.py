from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time

class Article:
    def __init__(self, title, content, source, url, publication_date):
        self.title = title
        self.content = content
        self.source = source
        self.url = url
        self.publication_date = publication_date

class JPostScraper:
    def __init__(self):
        self.base_url = "https://www.jpost.com"
        self.source_name = "The Jerusalem Post"
        self.options = Options()
        self.options.add_argument('--headless=new')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--window-size=1920,1080')
        self.options.binary_location = '/usr/bin/chromium-browser'
        self.options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    def get_driver(self):
        """Get a new Chrome driver instance"""
        service = ChromeService()
        return webdriver.Chrome(service=service, options=self.options)

    def scrape_article(self, url):
        """Scrape a single article"""
        driver = self.get_driver()
        try:
            print(f"\nScraping article from: {url}")
            
            driver.get(url)
            time.sleep(3)  # Wait for JavaScript to load
            
            print("Page title:", driver.title)
            print("Current URL:", driver.current_url)

            # Extract title
            title = ""
            try:
                title_elem = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'article-title'))
                )
                title = title_elem.text.strip()
                print(f"Found title: {title}")
            except Exception as e:
                print(f"Error finding title: {str(e)}")
                print("Available h1 tags:", [h1.get_attribute('class') for h1 in driver.find_elements(By.TAG_NAME, 'h1')])

            # Extract subtitle
            subtitle = ""
            try:
                subtitle_elem = driver.find_element(By.CLASS_NAME, 'article-subtitle')
                subtitle = subtitle_elem.text.strip()
                print(f"Found subtitle: {subtitle}")
            except Exception as e:
                print(f"Error finding subtitle: {str(e)}")
                print("Available h2 tags:", [h2.get_attribute('class') for h2 in driver.find_elements(By.TAG_NAME, 'h2')])

            # Extract content
            try:
                content_div = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'article-inner-content'))
                )
            except Exception as e:
                print(f"Error finding content: {str(e)}")
                print("Available sections:", [section.get_attribute('class') for section in driver.find_elements(By.TAG_NAME, 'section')])
                return None

            paragraphs = []
            if subtitle:
                paragraphs.append(f"<strong>{subtitle}</strong>")

            for p in content_div.find_elements(By.TAG_NAME, 'p'):
                text = p.text.strip()
                if text and len(text) > 20:  # Only keep substantial paragraphs
                    if not any(skip in text.lower() for skip in [
                        'advertisement', 'newsletter', 'subscribe to',
                        'promoted content', 'sponsored content'
                    ]):
                        paragraphs.append(text)

            if not paragraphs:
                print("No valid paragraphs found")
                return None

            content = '\n\n'.join(paragraphs)
            print(f"Total paragraphs found: {len(paragraphs)}")

            # Extract publication date
            pub_date = datetime.now()
            try:
                meta_tags = driver.find_elements(By.TAG_NAME, 'meta')
                for meta in meta_tags:
                    if meta.get_attribute('property') in ['article:published_time', 'og:article:published_time']:
                        date_str = meta.get_attribute('content')
                        if date_str:
                            pub_date = datetime.fromisoformat(date_str.split('+')[0].strip())
                            print(f"Found publication date: {pub_date}")
                            break
            except:
                pass

            # Create article
            article = Article(
                title=title,
                content=content,
                source=self.source_name,
                url=url,
                publication_date=pub_date
            )

            print(f"Successfully created article object")
            return article

        except Exception as e:
            print(f"Error scraping article: {str(e)}")
            return None
            
        finally:
            driver.quit()

if __name__ == '__main__':
    scraper = JPostScraper()
    url = 'https://www.jpost.com/israel-news/article-848610'  # Direct article URL
    print('Scraping single article...')
    article = scraper.scrape_article(url)
    if article:
        print(f'\nTitle: {article.title}')
        paragraphs = article.content.split('\n\n')
        print(f'First paragraph: {paragraphs[0]}')
        print(f'Total paragraphs: {len(paragraphs)}')
        print(f'Publication date: {article.publication_date}')