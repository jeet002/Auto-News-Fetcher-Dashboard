from django.core.management.base import BaseCommand
from news.services import NewsAPIService

class Command(BaseCommand):
    help = 'Fetches latest news from NewsAPI'
    
    def handle(self, *args, **options):
        try:
            service = NewsAPIService()
            news_data = service.fetch_news()
            saved_count = service.save_articles(news_data['articles'])
            
            self.stdout.write(
                self.style.SUCCESS(f'Successfully fetched {saved_count} new articles!')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error fetching news: {str(e)}')
            )