from typing import Any

import pydantic


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


class TitleSchema(pydantic.BaseModel):
    type: str
    text: TextSchema


class CreateDatabaseRequestSchema(pydantic.BaseModel):
    parent: ParentSchema
    title: TitleSchema
    icon: IconsSchema
    cover: CoverSchema
    properties: Any
