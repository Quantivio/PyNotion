from dotenv import load_dotenv

from config import base_config
from schema import NotionDatabaseResponseSchema
from schema.request import Filter, PropertyFilter, RichTextFilter
from src.pynotionclient import PyNotion

load_dotenv()
py_notion_client = PyNotion(token=base_config.notion_secret_token)

filter_dict = {"page_size": 100, "filter": {"property": "Name", "rich_text": {"contains": "Home"}}}

# Create necessary filter objects from Pydantic models and use them to query the database.

rich_text_filter = RichTextFilter(contains="Game")
property_filter = PropertyFilter(property="Name", rich_text=rich_text_filter)
filter_object = Filter(page_size=100, filter=property_filter)

response_dict_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(
    database_id=base_config.database_id, payload=filter_dict
)
response_filter_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(
    database_id=base_config.database_id, payload=filter_object
)
# # Since we are using pydantic the result can be used either as on object or as a dictionary or json.
# # This gives the user the flexibility to use the result as they wish.
# # Inside the properties use the key name you gave for each table in your database to access the value.
# # For example: CustomizedSelect is the key name for the table named "CustomizedSelect" in my database.
#
print(response_dict_payload.results[0].properties.CustomizedSelect.json(indent=4))  # Print the first result's Select property as json.
print(response_filter_payload.results[0].properties.CustomizedSelect.json(indent=4))  # Print the first result's Select property as json.
