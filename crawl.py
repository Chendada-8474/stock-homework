import requests
import urllib.parse
from datetime import date, datetime

TWSE_URL = "https://openapi.twse.com.tw"


class DailyStock:
    _STOCK_DAY_API = "/v1/exchangeReport/STOCK_DAY_AVG_ALL"

    def __init__(self, _test_response=None) -> None:
        self._request(_test_response)
        self._drop_ave_price()
        self._price_to_float()
        self._add_date(self.closing_date)

    def get_prices(self, stocks_symbols: list[str] = []) -> list[dict]:
        """
        Args:
            stocks_symbols: the list of target stock codes.
        Return:
            list of stock prices.
            format:
            [
                {"Code": str, "Name": str, "ClosingPrice": float, "ClosingDate": str ("%Y-%m-%d")},
                ...
            ]
        """

        if not stocks_symbols:
            return self._result
        return [self._result_map[code] for code in stocks_symbols]

    def is_code_available(self, code: str) -> bool:
        return code in self._result_map

    def _request(self, test_response=None):
        if not test_response:
            response = requests.get(self._STOCK_DAY_API_URL)
        else:
            response = test_response

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

    def _add_date(self, closing_date: date):
        dt = datetime.strftime(closing_date, "%Y-%m-%d")
        for stock in self._result:
            stock["ClosingDate"] = dt

    @property
    def _STOCK_DAY_API_URL(self) -> str:
        return urllib.parse.urljoin(TWSE_URL, self._STOCK_DAY_API)

    @property
    def closing_date(self) -> date:
        dt = datetime.strptime(
            self._response_headers["last-modified"], "%a, %d %b %Y %H:%M:%S %Z"
        )
        return dt.date()

    @property
    def code_list(self) -> list:
        return list(self._result_map.keys())
