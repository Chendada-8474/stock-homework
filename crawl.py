import requests
import urllib.parse
from datetime import date, datetime

TWSE_URL = "https://openapi.twse.com.tw"


class DailyStock:
    _STOCK_DAY_API = "/v1/exchangeReport/STOCK_DAY_AVG_ALL"

    def __init__(self) -> None:
        self._request()
        self._drop_ave_price()
        self._price_to_float()
        self._add_closing_date()

    def get_prices(self, stocks_symbols: list = []) -> list:
        if not stocks_symbols:
            return self._result()
        return [self._result_map[code] for code in stocks_symbols]

    def _request(self):
        response = requests.get(self._STOCK_DAY_API_URL)
        self._result = response.json()
        self._response_headers = response.headers
        self._result_map = self._symbol_as_key(self._result)

    def _symbol_as_key(self, results: dict) -> dict:
        symbol_key_results = {stock["Code"]: stock for stock in results}
        return symbol_key_results

    def _drop_ave_price(self):
        for stock in self._result:
            stock.pop("MonthlyAveragePrice")

    def _price_to_float(self):
        for stock in self._result:
            stock["ClosingPrice"] = (
                float(stock["ClosingPrice"]) if stock["ClosingPrice"] else None
            )

    def _add_closing_date(self):
        dt = datetime.strftime(self.price_date, "%Y-%m-%d")
        for stock in self._result:
            stock["ClosingDate"] = dt

    @property
    def _STOCK_DAY_API_URL(self) -> str:
        return urllib.parse.urljoin(TWSE_URL, self._STOCK_DAY_API)

    @property
    def price_date(self) -> date:
        dt = datetime.strptime(
            self._response_headers["last-modified"], "%a, %d %b %Y %H:%M:%S %Z"
        )
        return dt.date()
