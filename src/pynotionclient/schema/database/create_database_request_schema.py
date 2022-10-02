from typing import Any, List, Optional

import pydantic
from pydantic import validator

from pynotionclient.schema.database.content_schema import ContentSchema


class ParentSchema(pydantic.BaseModel):
    type: str
    page_id: str


class IconSchema(pydantic.BaseModel):
    type: str
    emoji: str

    @validator("type")
    def validate_emoji_type(cls, emoji_type):
        if emoji_type != "emoji":
            raise ValueError("Emoji type must be emoji")


class ExternalSchema(pydantic.BaseModel):
    url: str


class CoverSchema(pydantic.BaseModel):
    type: str
    external: ExternalSchema


class TextSchema(pydantic.BaseModel):
    content: str
    link: Optional[str]


class CreateDatabaseRequestSchema(pydantic.BaseModel):
    parent: ParentSchema
    title: List[ContentSchema]
    icon: IconSchema
    cover: CoverSchema
    properties: Any
