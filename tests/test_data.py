import sys
from datetime import date
from os.path import dirname


sys.path.append(dirname(dirname(__file__)))
from data import StockData


class TestStockData:
    stock_data = StockData(date(2023, 7, 18))

    def test_is_date_dup(self):
        case1 = self.stock_data.is_date_dup(date(2023, 7, 18))
        case2 = not self.stock_data.is_date_dup(date(2023, 7, 17))
        assert case1 and case2
