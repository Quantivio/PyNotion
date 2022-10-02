from typing import Any

import pydantic
from pydantic import validator

from pynotionclient.schema.database.request.content_configuration import (
    ContentConfiguration,
)


class ParentConfiguration(pydantic.BaseModel):
    type: str
    page_id: str


class IconConfiguration(pydantic.BaseModel):
    type: str
    emoji: str

    @validator("type")
    def validate_emoji_type(cls, emoji_type):
        if emoji_type != "emoji":
            raise ValueError("Emoji type must be emoji")


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
