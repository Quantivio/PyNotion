from typing import Any

import pydantic
from pydantic import field_validator

from .content_configuration import ContentConfiguration


class ParentConfiguration(pydantic.BaseModel):
	type: str
	page_id: str


class IconConfiguration(pydantic.BaseModel):
	type: str
	emoji: str

	@classmethod
	@field_validator("type")
	def validate_emoji_type(cls, emoji_type):  # type: ignore
		if emoji_type != "emoji":
			value_error = ValueError("Emoji type must be emoji")
			raise ValueError(value_error)


class ExternalConfiguration(pydantic.BaseModel):
	url: str


class CoverConfiguration(pydantic.BaseModel):
	type: str
	external: ExternalConfiguration


class DatabasePropertyConfiguration(pydantic.BaseModel):
	parent: ParentConfiguration
	title: list[ContentConfiguration]
	icon: IconConfiguration
	cover: CoverConfiguration
	properties: Any
