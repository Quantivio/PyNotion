
from dotenv import load_dotenv
from loguru import logger
from py_notion import PyNotion
from py_notion.schema.database import Filter, NotionDatabaseResponseSchema, PropertyFilter, RichTextFilter

from examples.config import base_config

load_dotenv()
py_notion_client = PyNotion(token=base_config.notion_secret_token)

filter_dict = {
	"page_size": 100,
	"filter": {"property": "Name", "rich_text": {"contains": "Home"}},
}

# Create necessary filter objects from Pydantic models and use them to query the database.

rich_text_filter = RichTextFilter(contains="Game")
property_filter = PropertyFilter(property="Name", rich_text=rich_text_filter)
filter_object = Filter(page_size=100, filter=property_filter)

response_dict_payload: NotionDatabaseResponseSchema | str = py_notion_client.database.query_database(
	database_id=base_config.database_id,
	payload=filter_dict,
)
response_filter_payload: NotionDatabaseResponseSchema | str = py_notion_client.database.query_database(
	database_id=base_config.database_id,
	payload=filter_object,
)

# Since we are using pydantic the result can be used either as on object or as a dictionary or json.
# This gives the user the flexibility to use the result as they wish.
# Inside the properties use the key name you gave for each table in your database to access the value.
# For example: CustomizedSelect is the key name for the table named "CustomizedSelect" in my database.
logger.info(response_filter_payload.model_dump_json(indent=4))

if isinstance(response_dict_payload, str):
	logger.info(response_dict_payload)

if isinstance(response_dict_payload, NotionDatabaseResponseSchema):
	logger.info(
		response_dict_payload.results[0].properties.Name.json(indent=4),
	)  # Print the first result's Select property as json.
if isinstance(response_filter_payload, NotionDatabaseResponseSchema):
	logger.info(
		response_filter_payload.results[0].properties.Name.json(indent=4),
	)  # Print the first result's Select property as json.
