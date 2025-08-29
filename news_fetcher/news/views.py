from django.shortcuts import render, redirect
from django.contrib import messages
from news.models import NewsArticle
from news.services import NewsAPIService

def dashboard(request):
    articles = NewsArticle.objects.all()[:20]  # Show latest 20 articles
    
    if request.method == 'POST' and 'fetch_news' in request.POST:
        try:
            service = NewsAPIService()
            news_data = service.fetch_news()
            saved_count = service.save_articles(news_data['articles'])
            messages.success(request, f'Successfully fetched {saved_count} new articles!')
        except Exception as e:
            messages.error(request, f'Error fetching news: {str(e)}')
        
        return redirect('dashboard')
    
    return render(request, 'news/dashboard.html', {'articles': articles})