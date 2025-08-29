import requests
from datetime import datetime
from django.conf import settings
from django.utils.timezone import make_aware

class NewsAPIService:
    BASE_URL = "https://newsapi.org/v2/top-headlines"
    
    def __init__(self):
        self.api_key = getattr(settings, 'NEWS_API_KEY', '')
    
    def fetch_news(self, category='general', country='us'):
        if not self.api_key:
            raise ValueError("NewsAPI key not configured")
        
        params = {
            'category': category,
            'country': country,
            'apiKey': self.api_key
        }
        
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def save_articles(self, articles_data):
        # Import here to avoid circular imports
        from news.models import NewsArticle
        
        saved_count = 0
        for article_data in articles_data:
            # Check if article already exists by title
            if NewsArticle.objects.filter(title=article_data['title']).exists():
                continue
            
            # Convert publishedAt string to datetime
            published_at = datetime.strptime(
                article_data['publishedAt'], 
                '%Y-%m-%dT%H:%M:%SZ'
            )
            
            # Make timezone aware
            published_at = make_aware(published_at)
            
            # Create and save article
            article = NewsArticle(
                title=article_data['title'],
                summary=article_data.get('description', ''),
                source=article_data['source']['name'],
                published_at=published_at,
                url=article_data['url'],
                url_to_image=article_data.get('urlToImage')
            )
            article.save()
            saved_count += 1
        
        return saved_count