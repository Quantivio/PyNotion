from typing import List, Any, Optional

import pydantic


class CreatedBySchema(pydantic.BaseModel):
    object: str
    id: str


class ParentSchema(pydantic.BaseModel):
    type: str
    database_id: Optional[str]


class InternalSelectSchema(pydantic.BaseModel):
    id: str
    name: str
    color: str


class SelectSchema(pydantic.BaseModel):
    id: str
    type: str
    select: InternalSelectSchema


class NumberSchema(pydantic.BaseModel):
    id: str
    type: str
    number: int


class PersonEmailSchema(pydantic.BaseModel):
    email: str


class PersonItemSchema(pydantic.BaseModel):
    object: str
    id: str
    name: str
    avatar_url: str
    type: str
    person: PersonEmailSchema


class PersonSchema(pydantic.BaseModel):
    id: str
    type: str
    people: List[PersonItemSchema]


class CheckboxSchema(pydantic.BaseModel):
    id: str
    type: str
    checkbox: bool


class MultiSelectItemSchema(pydantic.BaseModel):
    id: str
    name: str
    color: str


class TagsSchema(pydantic.BaseModel):
    id: str
    type: str
    multi_select: List[MultiSelectItemSchema]


class InternalStatusSchema(pydantic.BaseModel):
    id: str
    name: str
    color: str


class StatusSchema(pydantic.BaseModel):
    id: str
    type: str
    status: InternalStatusSchema


class InternalDateSchema(pydantic.BaseModel):
    start: str
    end: Any
    time_zone: Any


class DateSchema(pydantic.BaseModel):
    id: str
    type: str
    date: InternalDateSchema


class TextSchema(pydantic.BaseModel):
    content: str
    link: Any


class AnnotationsSchema(pydantic.BaseModel):
    bold: bool
    italic: bool
    strikethrough: bool
    underline: bool
    code: bool
    color: str


class TitleItemSchema(pydantic.BaseModel):
    type: str
    text: TextSchema
    annotations: AnnotationsSchema
    plain_text: str
    href: Any


class NameSchema(pydantic.BaseModel):
    id: str
    type: str
    title: List[TitleItemSchema]


# TODO: Add dynamic schema for properties
# class PropertiesSchema(pydantic.BaseModel):
#     select: SelectSchema = Field(alias="Select", title="Select")
#     number: NumberSchema = Field(alias="Number", title="Number")
#     person: PersonSchema = Field(alias="Person", title="Person")
#     checkbox: CheckboxSchema = Field(alias="", title="")
#     tags: TagsSchema = Field(alias="Tags", title="Tags")
#     status: StatusSchema = Field(alias="Status", title="Status")
#     date: DateSchema = Field(alias="Date", title="Date")
#     name: NameSchema = Field(alias="Name", title="Name")


class ResultSchema(pydantic.BaseModel):
    object: str
    id: str
    created_time: str
    last_edited_time: str
    created_by: CreatedBySchema
    last_edited_by: CreatedBySchema
    cover: Optional[Any]
    icon: Optional[Any]
    parent: ParentSchema
    archived: bool
    properties: Any  # TODO: PropertiesSchema
    has_more: bool
    type: str
    page: Any


class NotionDatabaseResponseSchema(pydantic.BaseModel):
    object: str
    results: List[ResultSchema]
