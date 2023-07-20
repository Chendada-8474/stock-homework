from yaml import load, Loader
from crawl import DailyStock
from data import StockData

with open("config.yaml") as file:
    config = load(file, Loader=Loader)


def run(request):
    stocks_latest = DailyStock()
    stock_data = StockData()

    if stock_data.is_date_dup(stocks_latest.closing_date):
        return "%s stock prices exist" % stock_data.latest_date

    stocks = stocks_latest.get_prices(config["target_stocks"])

    stock_data.insert(stocks)

    return "%s stock prices inserted" % stock_data.latest_date


if __name__ == "__main__":
    run(None)
