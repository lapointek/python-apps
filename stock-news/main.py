import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# 1.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "apikey": API_KEY,
    "symbol": STOCK_NAME,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in response_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

difference = abs(
    float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
)
print(difference)

diff_percent = (difference / float(yesterday_closing_price)) * 100
print(diff_percent)

# 2.
if diff_percent > 1:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]
print(articles)

three_articles = articles[:3]
print(three_articles)


# 3.
[
    f"Headline: {article['title']}. \nBrief: {article ['description']}"
    for articles in three_articles
]
