from pydantic import BaseSettings


# Create configuration with pydantic BaseSettings https://pydantic-docs.helpmanual.io/usage/settings/.
class Config(BaseSettings):
    notion_secret_token: str
    database_id: str
    page_id: str

    class Config:
        env_file = ".env"
        validate_assignment = True


base_config = Config()
