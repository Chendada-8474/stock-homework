import sys
import json
from os.path import dirname

sys.path.append(dirname(dirname(__file__)))
from crawl import DailyStock


class TestDailyStock:
    stock_today = DailyStock()

    def __init__(self) -> None:
        self.test_stocks = self._read_test_stocks()

    def _read_test_stocks(self):
        with open("./test_stocks.json") as f:
            test_stocks = json.load(f)
        return test_stocks
