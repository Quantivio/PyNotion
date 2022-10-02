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
