from typing import Any, List

import pydantic

from pynotionclient.schema.database import RichTextSchema


class ParentSchema(pydantic.BaseModel):
    type: str
    page_id: str


class IconsSchema(pydantic.BaseModel):
    type: str
    emoji: str


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
