import stock_data
import news_data
import notification

variation_percentage = stock_data.get_stock_change_percentage()
if abs(variation_percentage) >= 5:
    latest_news = news_data.get_stock_news()
    for article in latest_news:
        message = f"{stock_data.format_percentage(variation_percentage)}\nHeadline: {article['Headline']}\nBrief: {article['Brief']}"
        print(message)
        notification.send_sms(message)
