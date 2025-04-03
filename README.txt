# AI-Driven News Portal

An AI-powered news portal that aggregates news from Israeli sources and translates them into Russian. The portal features automated scraping, translation, and content rewriting capabilities.

## Features

- Automated news scraping from multiple Israeli news sources
- AI-powered translation from Hebrew to Russian
- Content rewriting for improved readability
- Modern, responsive web interface
- Article status tracking (pending, translated, rewritten, published)
- Admin interface for content management

## Technical Stack

- **Backend**: Django 5.2
- **Frontend**: Tailwind CSS
- **Database**: SQLite (development) / PostgreSQL (production)
- **Web Scraping**: BeautifulSoup4, Requests
- **Translation**: Custom translation service integration
- **Deployment**: Gunicorn

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd newsportal_project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

### Scraping Articles

To scrape new articles from configured sources:
```bash
python manage.py scrape_news
```

Options:
- `--dry-run`: Preview articles that would be scraped without saving

### Translating Articles

To translate pending articles:
```bash
python manage.py translate_articles
```

Options:
- `--article-id <id>`: Translate a specific article
- `--dry-run`: Preview articles that would be translated without saving

### Accessing the Portal

- Admin interface: `http://localhost:8000/admin/`
- Main site: `http://localhost:8000/`

## Project Structure

```
newsportal_project/
├── news/                      # Main application
│   ├── management/           # Management commands
│   │   └── commands/
│   │       ├── scrape_news.py
│   │       └── translate_articles.py
│   ├── templates/            # HTML templates
│   │   └── news/
│   │       ├── base.html
│   │       ├── article_list.html
│   │       └── article_detail.html
│   ├── models.py            # Database models
│   ├── views.py             # View controllers
│   ├── urls.py              # URL routing
│   ├── admin.py             # Admin interface
│   ├── tasks.py             # Scraping functionality
│   └── translation.py       # Translation functionality
├── newsportal_project/      # Project settings
├── static/                  # Static files
├── manage.py               # Django management script
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.