import unittest
from unittest.mock import patch, MagicMock
from news.scrapers.i24news_scraper import I24NewsScraper

class TestI24NewsScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = I24NewsScraper()
        self.test_url = "https://www.i24news.tv/en/news/israel/british-swedish-u-s-embassies-mark-25th-anniversary-of-stockholm-declaration"
        self.expected_data = {
            'title': "British, Swedish, U.S. embassies mark 25th anniversary of Stockholm Declaration",
            'content_snippets': [
                "Ahead of Israel's Holocaust Memorial Day",
                "British, Swedish, and U.S. embassies to the Jewish state held on Tuesday",
                "joint event at the British Ambassador's residence in Ramat Gan",
                "25th anniversary of the Stockholm Declaration",
                "International Holocaust Remembrance Alliance (IHRA)",
                "British Ambassador Simon Walters",
                "Swedish Ambassador Alexandra Rydmark",
                "U.S. Chargé d'Affaires Stephanie Hallett",
                "Michael Smuss (99), the last remaining survivor of the Warsaw Ghetto Uprising",
                "Holocaust remembrance and education is a collective responsibility"
            ]
        }
        
        # Mock HTML content
        self.mock_html = f"""
        <html>
            <head>
                <meta property="og:title" content="{self.expected_data['title']}" />
                <meta property="og:image" content="https://example.com/image.jpg" />
                <meta property="article:published_time" content="2024-01-16T12:00:00Z" />
            </head>
            <body>
                <div class="container container-page">
                    <h1>{self.expected_data['title']}</h1>
                    <div class="article-content">
                        <p>{self.expected_data['content_snippets'][0]}</p>
                        <p>{self.expected_data['content_snippets'][1]}</p>
                        <p>{self.expected_data['content_snippets'][2]}</p>
                        <p>{self.expected_data['content_snippets'][3]}</p>
                        <p>{self.expected_data['content_snippets'][4]}</p>
                        <p>{self.expected_data['content_snippets'][5]}</p>
                        <p>{self.expected_data['content_snippets'][6]}</p>
                        <p>{self.expected_data['content_snippets'][7]}</p>
                        <p>{self.expected_data['content_snippets'][8]}</p>
                        <p>{self.expected_data['content_snippets'][9]}</p>
                    </div>
                </div>
            </body>
        </html>
        """
        
    @patch('news.scrapers.i24news_scraper.RequestHandler')
    def test_article_scraping(self, mock_request_handler):
        """Test scraping an article from i24news using mock data."""
        # Setup mock response
        mock_response = MagicMock()
        mock_response.text = self.mock_html
        mock_request_handler_instance = MagicMock()
        mock_request_handler_instance.get.return_value = mock_response
        mock_request_handler.return_value = mock_request_handler_instance
        
        # Create new scraper instance with mocked request handler
        self.scraper = I24NewsScraper()
        
        # Test article scraping
        article = self.scraper.scrape_article(self.test_url)
        
        # Check if article data was retrieved
        self.assertIsNotNone(article)
        
        # Check required fields
        self.assertIn('title', article)
        self.assertIn('content', article)
        self.assertIn('source_url', article)
        self.assertIn('source_name', article)
        self.assertIn('pub_date', article)
        
        # Verify title
        self.assertEqual(article['title'], self.expected_data['title'])
        
        # Verify source name
        self.assertEqual(article['source_name'], 'i24NEWS')
        
        # Check content contains expected snippets
        content = article['content']
        for snippet in self.expected_data['content_snippets']:
            self.assertIn(snippet, content, f"Expected snippet not found: {snippet}")
        
        # Check URL
        self.assertEqual(article['source_url'], self.test_url)

if __name__ == '__main__':
    unittest.main()