from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


# Create configuration with pydantic BaseSettings https://pydantic-docs.helpmanual.io/usage/settings/.
class Config(BaseSettings):
	notion_secret_token: str = "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"
	database_id: str = "1258766a22dc80ea97bece3ce3a95e13"
	page_id: str = ""

	model_config = SettingsConfigDict(
		env_file=".env",
		env_file_encoding="utf-8",
	)


@lru_cache
def get_config() -> Config:
	return Config()


base_config = get_config()
