# news/apps.py
from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from news.services import NewsAPIService

class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    
    def ready(self):
        if not hasattr(self, 'scheduler'):
            self.scheduler = BackgroundScheduler()
            self.scheduler.add_job(
                self.fetch_news_job,
                'interval',
                hours=1,
                id='news_fetch_job',
                replace_existing=True
            )
            self.scheduler.start()
    
    def fetch_news_job(self):
        try:
            service = NewsAPIService()
            news_data = service.fetch_news()
            service.save_articles(news_data['articles'])
        except Exception as e:
            print(f"Error in scheduled news fetch: {str(e)}")