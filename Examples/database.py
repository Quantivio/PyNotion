from dotenv import load_dotenv

from config import base_config
from src.pynotionclient import PyNotion
from src.schema import NotionDatabaseResponseSchema

load_dotenv()
py_notion_client = PyNotion(token=base_config.notion_secret_token)
response: NotionDatabaseResponseSchema = py_notion_client.database.query_database(database_id=base_config.database_id)

# Since we are using pydantic the result can be used either as on object or as a dictionary or json.
# This gives the user the flexibility to use the result as they wish.
# Inside the properties use the key name you gave for each table in your database to access the value.
# For example: CustomizedSelect is the key name for the table named "CustomizedSelect" in my database.

print(response.dict())  # Print the response as a dictionary.
print(response.json())  # Print the response as json.
print(response.results[0].properties.CustomizedSelect.json(indent=4))  # Print the first result's Select property as json.
