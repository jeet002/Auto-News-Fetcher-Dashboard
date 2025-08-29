from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
from news.services import NewsAPIService

def fetch_news_job():
    try:
        service = NewsAPIService()
        news_data = service.fetch_news()
        service.save_articles(news_data['articles'])
        print(f"Scheduled news fetch completed successfully")
    except Exception as e:
        print(f"Error in scheduled news fetch: {str(e)}")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        fetch_news_job,
        'interval',
        hours=1,
        id='news_fetch_job',
        replace_existing=True
    )
    scheduler.start()
    print("Scheduler started!")