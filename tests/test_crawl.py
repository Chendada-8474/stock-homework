import sys
from datetime import date
from os.path import dirname


sys.path.append(dirname(dirname(__file__)))
from crawl import DailyStock
import tests.dataset


class TestDailyStock:
    test_response = tests.dataset.ResponseForTest()
    stocks = DailyStock(_test_response=test_response)

    def test_symbol_as_key(self):
        result_map = self.stocks._symbol_as_key(self.test_response.json())
        assert result_map == tests.dataset.result_map_for_test

    def test_drop_ave_price(self):
        assert all("MonthlyAveragePrice" not in stock for stock in self.stocks._result)

    def test_price_to_float(self):
        assert all(
            type(stock["ClosingPrice"]) == float
            for stock in self.stocks._result
            if stock["ClosingPrice"]
        )

    def test_add_date(self):
        assert all(
            "ClosingDate" in stock and stock["ClosingDate"] == "2023-07-18"
            for stock in self.stocks._result
        )

    def test_price_date(self):
        assert self.stocks.price_date == date(2023, 7, 18)

    def test_get_price(self):
        case1 = self._result_compare(
            self.stocks.get_prices(), tests.dataset.untarget_answer
        )
        case2 = self._result_compare(
            self.stocks.get_prices(stocks_symbols=["0050", "0051", "0052"]),
            tests.dataset.targeted_answer,
        )
        assert case1 and case2

    def _result_compare(self, result1, result2):
        for stock, test_stock in zip(result1, result2):
            for key in stock:
                if stock[key] != test_stock[key]:
                    return False
        return True
