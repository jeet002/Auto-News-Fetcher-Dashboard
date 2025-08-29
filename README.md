# Auto News Fetcher & Dashboard

A Django-based web application that automatically fetches the latest news headlines from NewsAPI and displays them in a clean, responsive dashboard.

## Features
- **Automated News Fetching**: Retrieves latest headlines from NewsAPI
- **Duplicate Prevention**: Ensures no duplicate articles are stored
- **Manual Trigger**: "Fetch Latest News" button for on-demand updates
- **Background Scheduler**: Automatic fetching every hour (using APScheduler)
- **Responsive UI**: Bootstrap-based dashboard that works on all devices
- **Management Command**: CLI command for manual news fetching

## Technology Stack
- **Backend**: Django 5.2.5
- **Database**: SQLite (default)
- **Frontend**: HTML5, Bootstrap 5.3
- **API**: NewsAPI.org
- **Scheduler**: APScheduler
- **Dependencies**: requests, python-dotenv

## Project Structure
news_fetcher/
├── news_fetcher/ # Django project settings
├── news/ # Main application
│ ├── management/
│ │ └── commands/
│ │ └── fetch_news.py # Management command
│ ├── migrations/ # Database migrations
│ ├── init.py
│ ├── admin.py # Admin configuration
│ ├── apps.py # App configuration with scheduler
│ ├── models.py # NewsArticle model
│ ├── scheduler.py # Background scheduler setup
│ ├── services.py # NewsAPI service class
│ ├── tests.py # Test cases
│ ├── urls.py # Application URLs
│ └── views.py # Dashboard view
├── templates/ # HTML templates
│ └── news/
│ └── dashboard.html
├── .env # Environment variables (create this)
├── .gitignore # Git ignore rules
├── manage.py # Django management script
├── requirements.txt # Python dependencies
└── README.md # This file


## Setup Instructions
1. Clone the Repository
 - git clone https://github.com/jeet002/Auto-News-Fetcher-Dashboard
 - cd news_fetcher
2. Create Virtual Environment
 - python -m venv venv
 - source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
 - pip install -r requirements.txt
4. Set Up Environment Variables
 - Create a .env file in the project root:
   - NEWS_API_KEY=your_actual_newsapi_key_here
 - Get your free API key from "NewsAPI.org".
5. Run Migrations
 - python manage.py migrate
6. Start Development Server
 - python manage.py runserver
 - Visit http://localhost:8000/ to see the application.


## How to Use
**Manual News Fetching via Web UI:-
  - Open the dashboard in your browser
  - Click the "Fetch Latest News" button
  - View the newly fetched articles on the dashboard
**Manual News Fetching via Command Line:-
  - python manage.py fetch_news
**Access Admin Interface:-
- Create a superuser first:
  - python manage.py createsuperuser
  - Then visit http://localhost:8000/admin/
 
##Screenshots

![image alt](https://github.com/jeet002/Auto-News-Fetcher-Dashboard/blob/cd939c04f278fbaa9795fc0f75e7cf4236ab307a/Auto_News_Fetcher_Dashboard.png)
