from typing import Any, List

import pydantic
from pydantic import validator

from pynotionclient.schema.database.rich_text_schema import RichTextSchema


class ParentSchema(pydantic.BaseModel):
    type: str
    page_id: str


class IconsSchema(pydantic.BaseModel):
    type: str
    emoji: str

    @validator
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
    link: pydantic.AnyUrl


class CreateDatabaseRequestSchema(pydantic.BaseModel):
    parent: ParentSchema
    title: List[RichTextSchema]
    icon: IconsSchema
    cover: CoverSchema
    properties: Any
