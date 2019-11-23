from typing import Any, Dict

from decouple import config

from utils.singleton import singleton


@singleton
class Config:
    def __init__(self):
        self._config: Dict[str, Any] = {
            "DEBUG": config("DEBUG", default="0", cast=bool),
            "TELEGRAM_API_TOKEN": config("TELEGRAM_API_TOKEN")
        }

    def __getitem__(self, item: str) -> Any:
        return self._config[item]