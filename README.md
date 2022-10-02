# PyNotion

<img src="assets/notion.png" alt="Notion Logo" height="64" width="64">
<br>

[![PyPI version](https://badge.fury.io/py/PyNotionclient.svg)](https://badge.fury.io/py/PyNotionclient)
[![Top Language](https://img.shields.io/github/languages/top/pythonhubdev/PyNotion)](https://img.shields.io/github/languages/top/pythonhubdev/PyNotion)
![GitHub last commit](https://img.shields.io/github/last-commit/pythonhubdev/PyNotion)
![PyPI - License](https://img.shields.io/pypi/l/pynotionclient)
![GitHub Repo stars](https://img.shields.io/github/stars/pythonhubdev/PyNotion?style=social)
[![Downloads](https://static.pepy.tech/personalized-badge/pynotionclient?period=month&units=international_system&left_color=black&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/pynotionclient)

### A Notion API wrapper for Python (In Development)

PyNotion is a simple-to-use and easy-to-understand API wrapper for [Notion.so](https://developers.notion.com/) Currently
in development and
supports the following features:

1. Create a new database
2. Get a database

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

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

#### 3. Creating a database

```python
from dotenv import load_dotenv

from examples.config import base_config
from pynotionclient import PyNotion
from pynotionclient.schema.database import (
    ParentConfiguration,
    IconConfiguration,
    TextConfiguration,
    ExternalConfiguration,
    CoverConfiguration,
    SelectOptionsConfiguration,
    SelecOptionsListConfig,
    TitleConfiguration,
    RichTextConfiguration,
    CheckboxConfiguration,
    SelectConfiguration,
    ContentConfiguration,
    MultiSelectConfiguration,
    NumberConfiguration,
    NumberFormats,
    NumberFormatConfiguration,
    DatabasePropertyConfiguration,
    )

load_dotenv()
py_notion_client = PyNotion(token=base_config.notion_secret_token)

# # Create database payload
parent_payload = ParentConfiguration(
        type="page_id", page_id=base_config.page_id
        )  # The parent is the page where the database will be created.
icon_payload = IconConfiguration(
        type="emoji", emoji="🎮"
        )  # The icon is the icon that will be displayed on the database.
text = TextConfiguration(
        content="Game"
        )  # The text is the text that will be displayed as the title of the database.
content = ContentConfiguration(
        type="text", plain_text="Game", href="https://www.google.com", text=text
        )  # The content has other info's of the title.

# Cover schema
cover = CoverConfiguration(
        type="external", external=ExternalConfiguration(url="https://www.google.com")
        )

# # Forming select options schema
properties = {
        "Name":        TitleConfiguration().dict(),
        "Description": RichTextConfiguration().dict(),
        "In stock":    CheckboxConfiguration().dict(),
        "Food Group":  SelectConfiguration(
                select=SelecOptionsListConfig(
                        options=[
                                SelectOptionsConfiguration(color="green", name="Code"),
                                SelectOptionsConfiguration(color="red", name="Game"),
                                ],
                        )
                ).dict(),
        "Cusines":     MultiSelectConfiguration(
                multi_select=SelecOptionsListConfig(
                        options=[
                                SelectOptionsConfiguration(color="green", name="Code"),
                                SelectOptionsConfiguration(color="red", name="Game"),
                                ],
                        )
                ).dict(),
        "Price":       NumberConfiguration(
                number=NumberFormatConfiguration(
                        format=NumberFormats.NUMBER_WITH_COMMAS,
                        ),
                ).dict(),
        }
print(properties)
create_database_payload = DatabasePropertyConfiguration(
        title=[content],
        cover=cover,
        parent=parent_payload,
        icon=icon_payload,
        properties=properties,
        )

response = py_notion_client.database.create_database(
        payload=create_database_payload,
        )

print(response.json())
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

