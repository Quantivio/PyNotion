from __future__ import annotations

from typing import Any

import pydantic
from pydantic import BaseModel

from src.py_notion.schema.database.request.database_property_configuration import (
	CoverConfiguration,  # noqa: TCH001
	IconConfiguration,  # noqa: TCH001
	ParentConfiguration,  # noqa: TCH001
)
from src.py_notion.schema.database.request.number_configuration import NumberFormats  # noqa: TCH001
from src.py_notion.schema.database.response.database_response_schema import DefaultSettingsSchema
from src.py_notion.schema.database.response.select_schema import InternalSelectSchema

from .content_schema import ContentSchema  # noqa: TCH001


class CreatedByResponseSchema(BaseModel):
	object: str
	id: str


class LastEditedByResponseSchema(BaseModel):
	object: str
	id: str


class Number(BaseModel):
	format: NumberFormats


class CreateDatabaseResponseSchema(BaseModel):
	object: str
	id: str
	cover: CoverConfiguration
	icon: IconConfiguration
	created_time: str
	created_by: CreatedByResponseSchema
	last_edited_by: LastEditedByResponseSchema
	last_edited_time: str
	title: list[ContentSchema]
	description: list[Any]
	is_inline: bool
	properties: Any = None
	parent: ParentConfiguration
	url: str
	archived: bool


class CommonCreateResponseSchema(BaseModel):
	id: str | None
	name: str | None
	type: str | None


def generate_dynamic_property_create_response_schema(properties: dict[str, Any]) -> type[CommonCreateResponseSchema]:
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
				key,
				__base__=CommonCreateResponseSchema,
				**{value["type"]: {}},
			)  # type: ignore
			properties_schema[key] = (common_dynamic_schema, defaults.model_dump())
		elif value["type"] in ["select", "multi_select"]:
			dynamic_select_schema = pydantic.create_model(
				key,
				__base__=CommonCreateResponseSchema,
				**{value["type"]: {"options": list[InternalSelectSchema]}},
			)  # type: ignore
			properties_schema[key] = (dynamic_select_schema, defaults.model_dump())
		elif value["type"] == "number":
			dynamic_number_schema = pydantic.create_model(
				key,
				__base__=CommonCreateResponseSchema,
				**{value["type"]: Number},
			)  # type: ignore
			properties_schema[key] = (dynamic_number_schema, defaults.model_dump())
	return pydantic.create_model("CreatePropertiesSchema", **properties_schema)  # type: ignore


def generate_dynamic_create_notion_response_schema(
	result_schema: Any,  # noqa: ANN401
) -> type[CreateDatabaseResponseSchema]:
	defaults = DefaultSettingsSchema(alias="results", title="results")
	return pydantic.create_model(
		"CreateDatabaseResponseSchema",
		__base__=CreateDatabaseResponseSchema,
		properties=(result_schema, defaults.model_dump()),
	)  # type: ignore
