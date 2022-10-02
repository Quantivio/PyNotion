from src.pynotionclient.config.constants import Constants


class Urls:
    @staticmethod
    def form_db_get_url(database_id: str) -> str:
        base_url: str = f"{Constants.DB_BASE_URL}/{database_id}/query"
        return base_url

    @staticmethod
    def form_pages_get_url(page_id: str) -> str:
        base_url: str = f"{Constants.PAGES_BASE_URL}/{page_id}"
        return base_url

    @staticmethod
    def form_block_get_url(block_id: str) -> str:
        base_url: str = f"{Constants.BLOCK_BASE_URL}/{block_id}"
        return base_url

    @staticmethod
    def form_user_get_url(user_id: str) -> str:
        base_url: str = f"{Constants.USERS_BASE_URL}/{user_id}"
        return base_url
