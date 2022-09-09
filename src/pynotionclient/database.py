import json

from requests import ReadTimeout, Timeout, ConnectTimeout

from schema import generate_dynamic_properties_schema, generate_dynamic_result_schema
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
            # response: Response = requests.post(url=Urls.form_db_get_url(database_id), headers=default_header_schema.dict(by_alias=True), timeout=60)
            # database_response: NotionDatabaseResponseSchema = NotionDatabaseResponseSchema(**response.json())

            # DynamicNotionDatabaseResponseSchema = create_model("DynamicNotionDatabaseResponseSchema", __base__=NotionDatabaseResponseSchema)
            with open("database_response.json", "r") as stored_respnse:
                json_data = json.loads(stored_respnse.read())
                properties: dict | None = None
                if len(json_data["results"][0]["properties"]) > 0:
                    properties = json_data["results"][0]["properties"]
                dynamic_properties_schema = generate_dynamic_properties_schema(properties)
                dynamic_result_schema = generate_dynamic_result_schema(dynamic_properties_schema)
                database_response = dynamic_result_schema(**json_data)
                print(database_response.results[0].properties.text.json())
        except (ConnectTimeout, Timeout, ReadTimeout) as time_out_exception:
            logger.error(message=f"Timeout error while querying", file_name=__name__, function_name=function_name)
            raise time_out_exception

    def __add_bearer_token(self):
        default_header_schema.authorization = default_header_schema.authorization + self.token
