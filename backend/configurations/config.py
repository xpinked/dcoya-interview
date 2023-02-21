import json

from dataclasses import dataclass
from pathlib import Path

__dir__ = Path(__file__).absolute().parent


@dataclass
class Settings:
    HOST: str
    PORT: int
    MONGO_DB_NAME: str
    MONGO_HOST: str
    MONGO_PORT: str
    MONGO_USER: str
    MONGO_PASSWORD: str
    LOG_LEVEL: int
    ALLOWED_ORIGINS: list[str]
    DEBUG: bool
    SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


class Config:
    settings_file = __dir__/'settings.json'

    @classmethod
    def load_settings(
        cls,
    ) -> Settings:

        with open(cls.settings_file, 'r',) as fp:
            _settings = json.load(
                fp=fp,
            )

        return Settings(**_settings)


if 'settings' not in globals():
    settings = Config.load_settings()
