from typing import Any

import pydantic
from pynotionclient.schema.database.response.check_box_schema import CheckboxSchema
from pynotionclient.schema.database.response.date_schema import DateSchema
from pynotionclient.schema.database.response.multi_select_schema import (
    MultiSelectSchema,
)
from pynotionclient.schema.database.response.number_schema import NumberSchema
from pynotionclient.schema.database.response.person_schema import PersonSchema
from pynotionclient.schema.database.response.result_schema import ResultSchema
from pynotionclient.schema.database.response.rich_text_schema import RichTextSchema
from pynotionclient.schema.database.response.select_schema import SelectSchema
from pynotionclient.schema.database.response.status_schema import StatusSchema
from pynotionclient.schema.database.response.title_schema import TitleSchema


class NotionDatabaseResponseSchema(pydantic.BaseModel):
    object: str
    results: list[ResultSchema]
    has_more: bool
    type: str
    page: Any = None


class DefaultSettingsSchema(pydantic.BaseModel):
    alias: str
    title: str
    required: bool = True


def generate_dynamic_properties_schema(properties_data: dict[str, Any]) -> Any:
    """Generate a dynamic schema model based on the keys received from Notions Response"""
    properties_schema = {}
    for key, value in properties_data.items():
        defaults = DefaultSettingsSchema(alias=key, title=key)
        if value["type"] == "select":
            properties_schema[key] = (SelectSchema, defaults.model_dump())
        elif value["type"] == "number":
            properties_schema[key] = (NumberSchema, defaults.model_dump())
        elif value["type"] == "people":
            properties_schema[key] = (PersonSchema, defaults.model_dump())
        elif value["type"] == "checkbox":
            properties_schema[key] = (CheckboxSchema, defaults.model_dump())
        elif value["type"] == "multi_select":
            properties_schema[key] = (MultiSelectSchema, defaults.model_dump())
        elif value["type"] == "status":
            properties_schema[key] = (StatusSchema, defaults.model_dump())
        elif value["type"] == "date":
            properties_schema[key] = (DateSchema, defaults.model_dump())
        elif value["type"] == "title":
            properties_schema[key] = (TitleSchema, defaults.model_dump())
        elif value["type"] == "rich_text":
            properties_schema[key] = (RichTextSchema, defaults.model_dump())
        else:
            raise ValueError(f"Unknown type: {value['type']}")

    return pydantic.create_model("PropertiesSchema", **properties_schema)  # type: ignore


def generate_dynamic_result_schema(properties_schema: Any) -> type[ResultSchema]:
    defaults = DefaultSettingsSchema(alias="properties", title="properties")
    return pydantic.create_model(
        "NotionDatabaseResponseSchema",
        __base__=ResultSchema,
        properties=(properties_schema, defaults.model_dump()),
    )  # type: ignore


def generate_dynamic_notion_response_schema(
    result_schema: Any,
) -> type[NotionDatabaseResponseSchema]:
    defaults = DefaultSettingsSchema(alias="results", title="results")
    return pydantic.create_model(
        "NotionDatabaseResponseSchema",
        __base__=NotionDatabaseResponseSchema,
        results=(list[result_schema], defaults.model_dump()),
    )
