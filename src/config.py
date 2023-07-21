import os
from yaml import load, Loader

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, "config.yaml")


class Config:
    def __init__(self, path) -> None:
        self._config = self._read(path)
        self._setattr_from_dict(self._config)

    def _read(self, path: str) -> dict:
        with open(path) as file:
            config = load(file, Loader=Loader)
        return config

    def _setattr_from_dict(self, config: dict):
        for k, v in config.items():
            setattr(self, k, v)


def read_config(path: str = CONFIG_PATH) -> Config:
    return Config(path)
