from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


# Create configuration with pydantic BaseSettings https://pydantic-docs.helpmanual.io/usage/settings/.
class Config(BaseSettings):
    notion_secret_token: str = ""
    database_id: str = ""
    page_id: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_config() -> Config:
    return Config()


base_config = get_config()
