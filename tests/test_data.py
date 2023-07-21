import sys
from datetime import date
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT_DIR)
from src.data import StockData


class TestStockData:
    stock_data = StockData(date(2023, 7, 18))

    def test_is_date_dup(self):
        case1 = self.stock_data.is_date_dup(date(2023, 7, 18))
        case2 = not self.stock_data.is_date_dup(date(2023, 7, 17))
        assert case1 and case2
