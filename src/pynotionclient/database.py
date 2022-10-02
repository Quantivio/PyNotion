from typing import Type

import requests
from requests import ReadTimeout, Timeout, ConnectTimeout, Response

from src.pynotionclient.config import Constants
from src.pynotionclient.config import Urls
from src.pynotionclient.schema.common.header_schema import default_header_schema
from src.pynotionclient.schema.database import Filter
from src.pynotionclient.schema.database import (
    NotionDatabaseResponseSchema,
)
from src.pynotionclient.schema.database import (
    ResultSchema,
)
from src.pynotionclient.schema.database.database_response_schema import (
    generate_dynamic_properties_schema,
    generate_dynamic_result_schema,
    generate_dynamic_notion_response_schema,
)
from src.pynotionclient.utils import logger


class NotionDatabase:
    def __init__(self, token: str):
        self.token = token
        self.__add_bearer_token()

    @staticmethod
    def query_database(database_id: str, payload: dict | Filter) -> NotionDatabaseResponseSchema:
        function_name: str = "Querying Notion database"
        logger.info(message=f"Querying database {database_id}", file_name=__name__, function_name=function_name)
        try:
            __payload: dict | str | None = None
            if type(payload) is dict:
                __payload = payload
            elif type(payload) is Filter:
                __payload = payload.dict(exclude_none=True, by_alias=True)
            response: Response = requests.post(
                url=Urls.form_db_get_url(database_id), json=__payload, headers=default_header_schema.dict(by_alias=True), timeout=60
            )
            json_data = response.json()
            properties: dict | None = None
            if json_data is not None and len(json_data["results"][0]["properties"]) > 0:
                properties = json_data["results"][0]["properties"]
            DynamicPropertiesSchema = generate_dynamic_properties_schema(properties)
            DynamicResultSchema: Type[ResultSchema] = generate_dynamic_result_schema(DynamicPropertiesSchema)
            DynamicNotionDatabaseResponseSchema: Type[NotionDatabaseResponseSchema] = generate_dynamic_notion_response_schema(DynamicResultSchema)
            database_response: NotionDatabaseResponseSchema = DynamicNotionDatabaseResponseSchema(**json_data)
            return database_response
        except (ConnectTimeout, Timeout, ReadTimeout) as time_out_exception:
            logger.error(message=f"Timeout error while querying", file_name=__name__, function_name=function_name)
            raise time_out_exception

    @staticmethod
    def create_database(payload: dict):
        function_name: str = "Creating Notion database"
        logger.info(message=f"Creating database", file_name=__name__, function_name=function_name)
        try:
            response: Response = requests.post(
                url=Constants.DB_BASE_URL,
                json=payload,
                headers=default_header_schema.dict(by_alias=True),
                timeout=60,
            )
            return response
        except (ConnectTimeout, Timeout, ReadTimeout) as time_out_exception:
            logger.error(message=f"Timeout error while creating database", file_name=__name__, function_name=function_name)
            raise time_out_exception

    def __add_bearer_token(self):
        default_header_schema.authorization = default_header_schema.authorization + self.token
