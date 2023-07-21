import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT_DIR)
from src.config import Config


class TestConfig:
    test_config_path = os.path.join(os.path.dirname(__file__), "test_config.yaml")
    test_config_dict = {
        "target_stocks": ["0050", "2330"],
        "gcp_auth_json": "test_api_key.json",
        "table_name": "test_project.test_dataset.test_table",
    }

    config = Config(path=test_config_path)

    def test_setattr_from_dict(self):
        case1 = self.config.target_stocks == ["0050", "2330"]
        case2 = self.config.gcp_auth_json == "test_api_key.json"
        case3 = self.config.table_name == "test_project.test_dataset.test_table"
        assert all((case1, case2, case3))

    def test_read(self):
        assert self.config._read(self.test_config_path) == self.test_config_dict
