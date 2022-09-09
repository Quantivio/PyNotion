from typing import List, Any, Optional, Type

import pydantic
from pydantic import create_model, Field


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


class MentionSchema(pydantic.BaseModel):
    type: str
    database: Any


class UserSchema(pydantic.BaseModel):
    object: str
    id: str
    name: str
    avatar_url: str
    type: str
    person: PersonEmailSchema


class UserMentionSchema(pydantic.BaseModel):
    type: str
    user: UserSchema


class TitleSchema(pydantic.BaseModel):
    type: str
    mention: UserMentionSchema


class TitleItemSchema(pydantic.BaseModel):
    type: str
    text: Optional[TextSchema]
    title: Optional[TitleSchema]
    mention: Optional[MentionSchema]
    annotations: AnnotationsSchema
    plain_text: str
    href: Any


class TitleTypeSchema(pydantic.BaseModel):
    id: str
    type: str
    title: List[TitleItemSchema]


class TextContentSchema(pydantic.BaseModel):
    id: str
    type: str
    rich_text: List[TitleItemSchema]


class PropertiesSchema(pydantic.BaseModel):
    select: SelectSchema = Field(alias="Select", title="Select")
    number: NumberSchema = Field(alias="Number", title="Number")
    person: PersonSchema = Field(alias="Person", title="Person")
    checkbox: Optional[CheckboxSchema] = Field(alias="", title="")
    tags: TagsSchema = Field(alias="Tags", title="Tags")
    status: StatusSchema = Field(alias="Status", title="Status")
    date: DateSchema = Field(alias="Date", title="Date")
    name: TitleTypeSchema = Field(alias="Name", title="Name")
    text: TextContentSchema = Field(alias="Text", title="Text")


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
    properties: PropertiesSchema


class NotionDatabaseResponseSchema(pydantic.BaseModel):
    object: str
    results: List[ResultSchema]
    has_more: bool
    type: str
    page: Any


class DefaultSettingsSchema(pydantic.BaseModel):
    alias: str
    title: str
    required: bool = True


def generate_dynamic_properties_schema(properties_data: dict) -> Type[PropertiesSchema]:
    """Generate a dynamic schema model based on the keys recieved from Notions Response """
    properties_schema = {}
    for key, value in properties_data.items():
        defaults = DefaultSettingsSchema(alias=key, title=key)
        if value["type"] == "select":
            properties_schema[key] = (SelectSchema, defaults.dict())
        elif value["type"] == "number":
            properties_schema[key] = (NumberSchema, defaults.dict())
        elif value["type"] == "people":
            properties_schema[key] = (PersonSchema, defaults.dict())
        elif value["type"] == "checkbox":
            properties_schema[key] = (CheckboxSchema, defaults.dict())
        elif value["type"] == "multi_select":
            properties_schema[key] = (TagsSchema, defaults.dict())
        elif value["type"] == "status":
            properties_schema[key] = (StatusSchema, defaults.dict())
        elif value["type"] == "date":
            properties_schema[key] = (DateSchema, defaults.dict())
        elif value["type"] == "title":
            properties_schema[key] = (TitleTypeSchema, defaults.dict())
        elif value["type"] == "rich_text":
            properties_schema[key] = (TextContentSchema, defaults.dict())
        else:
            raise ValueError(f"Unknown type: {value['type']}")

    return create_model("PropertiesSchema", **properties_schema)


def generate_dynamic_result_schema(properties_schema: Type[PropertiesSchema]):
    defaults = DefaultSettingsSchema(alias="properties", title="properties")
    return create_model("NotionDatabaseResponseSchema", __base__=NotionDatabaseResponseSchema, properties=(properties_schema, defaults.dict()))
