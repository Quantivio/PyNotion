import requests
from requests import Response, ReadTimeout, Timeout, ConnectTimeout

from src.config import Urls
from src.schema import default_header_schema
from src.utils import logger


class NotionDatabase:
    def __init__(self, token: str):
        self.token = token

    def query_database(self, database_id: str):
        function_name: str = "Querying Notion Database"
        try:
            self.__add_bearer_token()
            logger.info(message=f"Querying database {database_id}", file_name=__name__, function_name=function_name)
            response: Response = requests.post(url=Urls.form_db_get_url(database_id), headers=default_header_schema.dict(by_alias=True), timeout=60)
        except (ConnectTimeout, Timeout, ReadTimeout) as time_out_exception:
            logger.error(message=f"Timeout error while querying", file_name=__name__, function_name=function_name)
            raise time_out_exception

    def __add_bearer_token(self):
        default_header_schema.authorization = default_header_schema.authorization + self.token
