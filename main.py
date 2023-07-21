from src.crawl import DailyStock
from src.data import StockData
from src.config import read_config


config = read_config()


def run(request):
    stocks_latest = DailyStock()
    stock_data = StockData()

    if stock_data.is_date_dup(stocks_latest.closing_date):
        return "%s stock prices exist" % stock_data.latest_date

    stocks = stocks_latest.get_prices(config.target_stocks)

    stock_data.insert(stocks)

    return "%s stock prices inserted" % stock_data.latest_date


if __name__ == "__main__":
    run(None)
