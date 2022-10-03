from __future__ import annotations

from typing import Any, Optional

import pydantic

from pynotionclient.schema.database.request.database_property_configuration import (
    CoverConfiguration,
    IconConfiguration,
    ParentConfiguration,
)
from pynotionclient.schema.database.request.number_configuration import NumberFormats
from pynotionclient.schema.database.response.content_schema import ContentSchema
from pynotionclient.schema.database.response.database_response_schema import (
    DefaultSettingsSchema,
)
from pynotionclient.schema.database.response.select_schema import InternalSelectSchema


class CreatedByResponseSchema(pydantic.BaseModel):
    object: str
    id: str


class LastEditedByResponseSchema(pydantic.BaseModel):
    object: str
    id: str


class Number(pydantic.BaseModel):
    format: NumberFormats


class CreateDatabaseResponseSchema(pydantic.BaseModel):
    object: str
    id: str
    cover: CoverConfiguration
    icon: IconConfiguration
    created_time: str
    created_by: CreatedByResponseSchema
    last_edited_by: LastEditedByResponseSchema
    last_edited_time: str
    title: list[ContentSchema]
    description: list
    is_inline: bool
    properties: Any
    parent: ParentConfiguration
    url: str
    archived: bool


class CommonCreateResponseSchema(pydantic.pydantic.BaseModel):
    id: Optional[str]
    name: Optional[str]
    type: Optional[str]


def generate_dynamic_property_create_response_schema(properties: dict):
    properties_schema = {}
    for key, value in properties.items():
        defaults = DefaultSettingsSchema(alias=key, title=key)
        if value["type"] in [
            "checkbox",
            "date",
            "rich_text",
            "title",
            "url",
            "people",
            "file",
            "email",
            "phone_number",
            "created_time",
            "created_by",
            "last_edited_time",
            "last_edited_by",
        ]:
            common_dynamic_schema = pydantic.create_model(
                key, __base__=CommonCreateResponseSchema, **{value["type"]: {}}
            )
            properties_schema[key] = (common_dynamic_schema, defaults.dict())
        elif value["type"] in ["select", "multi_select"]:
            dynamic_select_schema = pydantic.create_model(
                key,
                __base__=CommonCreateResponseSchema,
                **{value["type"]: {"options": list[InternalSelectSchema]}},
            )
            properties_schema[key] = (dynamic_select_schema, defaults.dict())
        elif value["type"] == "number":
            dynamic_number_schema = pydantic.create_model(
                key, __base__=CommonCreateResponseSchema, **{value["type"]: Number}
            )
            properties_schema[key] = (dynamic_number_schema, defaults.dict())
    return pydantic.create_model("CreatePropertiesSchema", **properties_schema)


def generate_dynamic_create_notion_response_schema(
    result_schema: Any,
) -> type[CreateDatabaseResponseSchema]:
    defaults = DefaultSettingsSchema(alias="results", title="results")
    return pydantic.create_model(
        "CreateDatabaseResponseSchema",
        __base__=CreateDatabaseResponseSchema,
        properties=(result_schema, defaults.dict()),
    )
