from yaml import load, Loader
from crawl import DailyStock
from data import StockData


with open("config.yaml") as file:
    config = load(file, Loader=Loader)


def main():
    stocks_today = DailyStock()
    stock_data = StockData()

    if stock_data.is_date_dup(stocks_today.price_date):
        return

    stocks = stocks_today.get_prices(config["target_stocks"])

    stock_data.insert(stocks)


if __name__ == "__main__":
    main()
