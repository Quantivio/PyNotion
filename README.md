# PyNotion

<img src="assets/notion.png" alt="Notion Logo" height="64" width="64">
<br>

### A Notion API wrapper for Python (In Development)

> Simple to use and easy to understand API wrapper for Notion.so
>
>Curently in development and supports the following features:
> 1. Create a new database (Work in progress can create datbase passing payload as a dictionary)
> 2. Get a database

## Installation

`poetry add pynotionclient`

`pip install pynotionclient`

## Usage

```python
from pynotionclient import PyNotion
from examples.config import base_config
from pynotionclient.schema.database import RichTextFilter, PropertyFilter, Filter, NotionDatabaseResponseSchema

py_notion_client = PyNotion(token=base_config.notion_secret_token)

# Create necessary properties as dictionary
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
```

## Querying a Database

#### 1. Querying a database using a dictionary

```python
from pynotionclient import PyNotion
from examples.config import base_config
from pynotionclient.schema.database import NotionDatabaseResponseSchema
py_notion_client = PyNotion(token=base_config.notion_secret_token)

# Create necessary properties as dictionary
filter_dict = {"page_size": 100, "filter": {"property": "Name", "rich_text": {"contains": "Home"}}}
response_dict_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(
        database_id=base_config.database_id, payload=filter_dict
        )
```

#### 2. Querying a database using a Pydantic model

```python
from pynotionclient import PyNotion
from examples.config import base_config
from pynotionclient.schema.database import RichTextFilter, PropertyFilter, Filter, NotionDatabaseResponseSchema
py_notion_client = PyNotion(token=base_config.notion_secret_token)

# Create necessary filter objects from Pydantic models and use them to query the database.

rich_text_filter = RichTextFilter(contains="Game")
property_filter = PropertyFilter(property="Name", rich_text=rich_text_filter)
filter_object = Filter(page_size=100, filter=property_filter)

response_filter_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(
        database_id=base_config.database_id, payload=filter_object)
```

#### Response for querying a database

> Pynotionclient gives you the response as a Pydantic model. You can access the response as a dictionary or as a
> Pydantic model. The response is a NotionDatabaseResponseSchema model which has the following
> properties: https://developers.notion.com/reference/database

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.