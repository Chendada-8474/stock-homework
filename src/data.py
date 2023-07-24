import os
from datetime import date
from google.cloud import bigquery
from src.config import read_config

config = read_config()
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, "config.yaml")

if os.path.exists(CONFIG_PATH):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config.gcp_auth_json


class StockData:
    _table_name = config.table_name

    def __init__(self, _test_date: date = None) -> None:
        if not _test_date:
            self._client = bigquery.Client()
        self.latest_date = _test_date

    def is_date_dup(self, date: date) -> bool:
        """
        Args:
            date: A datetime.date to check for duplication with the last date.
        Return: True if duplicated with last date, vice versa False.
        """
        if not self.latest_date:
            self.latest_date = self._get_last_date()

        return date == self.latest_date

    def _get_last_date(self) -> date:
        query = f"SELECT MAX(ClosingDate) AS last_date FROM {self._table_name}"
        query_job = self._client.query(query)

        for row in query_job:
            return row[0]

        return None

    def insert(self, rows: list):
        errors = self._client.insert_rows_json(self._table_name, rows)
        return errors
