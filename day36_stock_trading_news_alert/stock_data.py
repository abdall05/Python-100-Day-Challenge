import requests
import os
from dotenv import load_dotenv, find_dotenv
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}


def get_stock_change_percentage():
    stock_response = requests.get(STOCK_ENDPOINT, stock_parameters)
    stock_response.raise_for_status()
    data = stock_response.json()
    today_date = dt.date.today()
    daily_data = data["Time Series (Daily)"]
    previous_4_days = [str(today_date - dt.timedelta(days=day)) for day in range(1, 5)]
    previous_2_days_close_price = []
    for day in previous_4_days:
        if day in daily_data and len(previous_2_days_close_price) < 2:
            previous_2_days_close_price.append(float(daily_data[day]["4. close"]))

    price_difference = previous_2_days_close_price[0] - previous_2_days_close_price[1]
    variation_percentage = price_difference * 100 / previous_2_days_close_price[0]
    return variation_percentage


def format_percentage(variation_percentage):
    if variation_percentage > 0:
        return f"{STOCK}: 🔺{variation_percentage:.2f}"

    elif variation_percentage < 0:
        return f"{STOCK}: 🔻{variation_percentage:.2f}"
