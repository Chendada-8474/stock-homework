import os
from datetime import date
from yaml import load, Loader
from google.cloud import bigquery

with open("config.yaml") as file:
    config = load(file, Loader=Loader)


if config["gcp_auth_json"] in os.listdir():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config["gcp_auth_json"]


class StockData:
    _table_name = config["table_name"]

    def __init__(self, _test_date: date = None) -> None:
        self.last_date = _test_date if _test_date else self._get_last_date()
        self._client = bigquery.Client() if _test_date else None

    def is_date_dup(self, date: date) -> bool:
        return date == self.last_date

    def _get_last_date(self) -> date:
        query = f"SELECT MAX(ClosingDate) AS last_date FROM {self._table_name}"
        query_job = self._client.query(query)

        for row in query_job:
            return row[0]

        return None

    def insert(self, rows: list):
        errors = self._client.insert_rows_json(self._table_name, rows)
        return errors
