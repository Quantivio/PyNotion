from typing import Any

import requests
from requests import ConnectTimeout, ReadTimeout, Response, Timeout

from pynotionclient.config import Constants, Urls
from pynotionclient.schema.common.header_schema import default_header_schema
from pynotionclient.schema.database import (
    DatabasePropertyConfiguration,
    Filter,
    NotionDatabaseResponseSchema,
    ResultSchema,
)
from pynotionclient.schema.database.response.create_database_response_schema import (
    CreateDatabaseResponseSchema,
    generate_dynamic_create_notion_response_schema,
    generate_dynamic_property_create_response_schema,
)
from pynotionclient.schema.database.response.database_response_schema import (
    generate_dynamic_notion_response_schema,
    generate_dynamic_properties_schema,
    generate_dynamic_result_schema,
)
from pynotionclient.utils import logger


class NotionDatabase:
    def __init__(self, token: str):
        self.token = token
        self.__add_bearer_token()

    @staticmethod
    def query_database(
        database_id: str,
        payload: dict[str, Any] | Filter,
        return_json: bool = False,
    ) -> NotionDatabaseResponseSchema | str:
        function_name: str = "Querying Notion database"
        logger.info(
            message=f"Querying database {database_id}",
            file_name=__name__,
            function_name=function_name,
        )
        try:
            __payload: dict[str, Any] | str | None = None
            if isinstance(payload, dict):
                __payload = payload
            elif isinstance(payload, Filter):
                __payload = payload.model_dump(exclude_none=True, by_alias=True)
            response: Response = requests.post(
                url=Urls.form_db_get_url(database_id),
                json=__payload,
                headers=default_header_schema.model_dump(by_alias=True),
                timeout=60,
            )
            json_data = response.json()
            properties: dict[str, Any] = {}
            if json_data is not None and len(json_data["results"][0]["properties"]) > 0:
                properties = json_data["results"][0]["properties"]
            dynamic_properties_schema = generate_dynamic_properties_schema(properties)
            dynamic_result_schema: type[ResultSchema] = generate_dynamic_result_schema(dynamic_properties_schema)
            dynamic_notion_database_response_schema: type[NotionDatabaseResponseSchema] = (
                generate_dynamic_notion_response_schema(dynamic_result_schema)
            )
            database_response: NotionDatabaseResponseSchema = dynamic_notion_database_response_schema(**json_data)
            if return_json:
                return database_response.model_dump_json()
            else:
                return database_response
        except (ConnectTimeout, Timeout, ReadTimeout) as time_out_exception:
            logger.error(
                message="Timeout error while querying",
                file_name=__name__,
                function_name=function_name,
            )
            raise time_out_exception

    @staticmethod
    def create_database(
        payload: dict[str, Any] | DatabasePropertyConfiguration,
        return_json: bool = False,
    ) -> CreateDatabaseResponseSchema | str:
        function_name: str = "Creating Notion database"
        logger.info(
            message="Creating database",
            file_name=__name__,
            function_name=function_name,
        )
        try:
            __payload: dict[str, Any] | str | None = None
            if isinstance(payload, dict):
                __payload = payload
            elif isinstance(payload, DatabasePropertyConfiguration):
                __payload = payload.model_dump(exclude_none=True, by_alias=True)
            response: Response = requests.post(
                url=Constants.DB_BASE_URL,
                json=__payload,
                headers=default_header_schema.model_dump(by_alias=True),
                timeout=60,
            )
            json_data = response.json()
            properties: dict[str, Any] = {}
            if json_data and json_data["properties"]:
                properties = json_data["properties"]
            generate_dynamic_property_response_schema = generate_dynamic_property_create_response_schema(properties)
            dynamic_create_notion_database_response_schema: type[CreateDatabaseResponseSchema] = (
                generate_dynamic_create_notion_response_schema(generate_dynamic_property_response_schema)
            )
            database_response: CreateDatabaseResponseSchema = dynamic_create_notion_database_response_schema(
                **json_data,
            )
            if return_json:
                return database_response.model_dump_json()
            else:
                return database_response
        except (ConnectTimeout, Timeout, ReadTimeout) as time_out_exception:
            logger.error(
                message="Timeout error while creating database",
                file_name=__name__,
                function_name=function_name,
            )
            raise time_out_exception

    def __add_bearer_token(self) -> None:
        default_header_schema.authorization = default_header_schema.authorization + self.token
