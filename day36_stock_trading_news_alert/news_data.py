import os
from dotenv import load_dotenv, find_dotenv

import requests

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "searchIn": "title",
    "sortBy": "publishedAt"
}


def get_stock_news():
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    latest_stock_news = [{"Headline": data['articles'][i]['title'], "Brief": data['articles'][i]['description']} for i
                         in range(3)]
    return latest_stock_news
