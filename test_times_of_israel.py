import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsportal_project.settings')
django.setup()

from bs4 import BeautifulSoup
from news.scrapers.times_of_israel_scraper import TimesOfIsraelScraper
from unittest.mock import MagicMock
from django.utils import timezone
from news.models import Article

def test_times_of_israel_scraper():
    # Clean up any existing test articles
    Article.objects.filter(url="https://www.timesofisrael.com/test-article/").delete()
    
    scraper = TimesOfIsraelScraper()
    mock_response = MagicMock()
    mock_response.text = """
    <html>
        <head><meta property="article:published_time" content="2025-04-02T10:00:00+00:00"></head>
        <body>
            <h1 class="headline">Western Wall cleared of thousands of visitors' notes ahead of Passover</h1>
            <h2 class="underline">According to the Western Wall Heritage Foundation, notes include messages sent through its website by people from enemy countries, such as Iran and Yemen</h2>
            <div class="the-content">
                <p>Thousands of notes and messages left by visitors from Israel and across the world in the past months were removed from the Western Wall in Jerusalem on Wednesday, days ahead of the Jewish holiday of Passover that begins April 12.</p>
                <p>The staff of the Western Wall Heritage Foundation, which manages the holy site, cleared the spaces between the millennia-old stones. The pieces of paper were transferred for ritual burial in a geniza site on the Mount of Olives. Jewish law requires that documents bearing the Hebrew name of God be disposed of by burying them in a designated area in a Jewish cemetery or synagogue.</p>
                <p>The cracks between the Wall's stones are cleared every six months, ahead of Passover and Rosh Hashanah.</p>
                <p>"This year, we have many prayers and wishes by soldiers, wounded, bereaved families and families who went through the terrible catastrophe of the Simhat Torah festival [on October 7, 2023], and the ensuing war," Western Wall Rabbi Shmuel Rabinowitz said in a video statement. "Hundreds of them visited here, while many sent them to us."</p>
                <p>The foundation allows people to send messages to be inserted into the Western Wall through its website.</p>
                <p>According to the foundation, this year, they received tens of thousands of notes by people all over the world, including countries that are at war with Israel, such as Iran, Yemen and Lebanon.</p>
                <p>Located in the heart of Jerusalem's Old City, the Western Wall is the last intact vestige of the Jewish Temple, which was destroyed by the Romans in 70 CE.</p>
            </div>
        </body>
    </html>
    """
    
    # Extract content
    soup = BeautifulSoup(mock_response.text, 'lxml')
    title, paragraphs = scraper.extract_content(soup)
    
    print("\nTITLE:")
    print("-" * 80)
    print(title)
    
    print("\nPARAGRAPHS:")
    print("-" * 80)
    for i, p in enumerate(paragraphs, 1):
        print(f"\n{i}.")
        print(p)
        print("-" * 80)
    
    # Create and save article
    article = Article(
        title=title,
        content="\n\n".join(paragraphs),
        source=scraper.source_name,
        original_language='en',
        publication_date=timezone.now(),
        status='pending',
        url="https://www.timesofisrael.com/test-article/"
    )
    
    print("\nSaving to database...")
    article.save()
    
    # Verify in database
    saved = Article.objects.get(url="https://www.timesofisrael.com/test-article/")
    print(f"Article saved with ID: {saved.id}")
    print(f"Total paragraphs: {len(saved.content.split(chr(10) + chr(10)))}")

if __name__ == "__main__":
    test_times_of_israel_scraper()