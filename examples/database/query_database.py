from dotenv import load_dotenv

from examples.config import base_config
from pynotionclient import PyNotion
from pynotionclient.schema.database import (
    RichTextFilter,
    PropertyFilter,
    Filter,
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
)

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

# response_dict_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(
#     database_id=base_config.database_id, payload=filter_dict
# )
# response_filter_payload: NotionDatabaseResponseSchema = py_notion_client.database.query_database(
#     database_id=base_config.database_id, payload=filter_object
# )

# # Since we are using pydantic the result can be used either as on object or as a dictionary or json.
# # This gives the user the flexibility to use the result as they wish.
# # Inside the properties use the key name you gave for each table in your database to access the value.
# # For example: CustomizedSelect is the key name for the table named "CustomizedSelect" in my database.

# print(response_dict_payload.results[0].properties.Name.json(indent=4))  # Print the first result's Select property as json.
# print(response_filter_payload.results[0].properties.Name.json(indent=4))  # Print the first result's Select property as json.

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
    "Name": TitleConfiguration().dict(),
    "Description": RichTextConfiguration().dict(),
    "In stock": CheckboxConfiguration().dict(),
    "Food Group": SelectConfiguration(
        select=SelecOptionsListConfig(
            options=[
                SelectOptionsConfiguration(color="green", name="Code"),
                SelectOptionsConfiguration(color="red", name="Game"),
            ],
        )
    ).dict(),
    "Cusines": MultiSelectConfiguration(
        multi_select=SelecOptionsListConfig(
            options=[
                SelectOptionsConfiguration(color="green", name="Code"),
                SelectOptionsConfiguration(color="red", name="Game"),
            ],
        )
    ).dict(),
    "Price": NumberConfiguration(
        number=NumberFormatConfiguration(
            format=NumberFormats.NUMBER_WITH_COMMAS,
        ),
    ).dict(),
}
print(properties)
# create_database_payload = DatabasePropertyConfiguration(
#         title=[content],
#         cover=cover,
#         parent=parent_payload,
#         icon=icon_payload,
#         properties=properties,
#         )
#
# response = py_notion_client.database.create_database(
#         payload=create_database_payload,
#         )
#
# print(response.json())
