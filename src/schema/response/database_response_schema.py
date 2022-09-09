from typing import List, Any, Optional, Type

import pydantic
from pydantic import create_model, Field

from schema.response.check_box_schema import CheckboxSchema
from schema.response.date_schema import DateSchema
from schema.response.multi_select_schema import MultiSelectSchema
from schema.response.number_schema import NumberSchema
from schema.response.person_schema import PersonSchema
from schema.response.rich_text_schema import RichTextSchema
from schema.response.select_schema import SelectSchema
from schema.response.status_schema import StatusSchema
from schema.response.title_schema import TitleSchema


class AuthoredBySchema(pydantic.BaseModel):
    object: str
    id: str


class ParentSchema(pydantic.BaseModel):
    type: str
    database_id: Optional[str]


class PropertiesSchema(pydantic.BaseModel):
    select: SelectSchema = Field(alias="Select", title="Select")
    number: NumberSchema = Field(alias="Number", title="Number")
    person: PersonSchema = Field(alias="Person", title="Person")
    checkbox: Optional[CheckboxSchema] = Field(alias="", title="")
    tags: MultiSelectSchema = Field(alias="Tags", title="Tags")
    status: StatusSchema = Field(alias="Status", title="Status")
    date: DateSchema = Field(alias="Date", title="Date")
    name: TitleSchema = Field(alias="Name", title="Name")
    text: RichTextSchema = Field(alias="Text", title="Text")


class ResultSchema(pydantic.BaseModel):
    object: str
    id: str
    created_time: str
    last_edited_time: str
    created_by: AuthoredBySchema
    last_edited_by: AuthoredBySchema
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
            properties_schema[key] = (MultiSelectSchema, defaults.dict())
        elif value["type"] == "status":
            properties_schema[key] = (StatusSchema, defaults.dict())
        elif value["type"] == "date":
            properties_schema[key] = (DateSchema, defaults.dict())
        elif value["type"] == "title":
            properties_schema[key] = (TitleSchema, defaults.dict())
        elif value["type"] == "rich_text":
            properties_schema[key] = (RichTextSchema, defaults.dict())
        else:
            raise ValueError(f"Unknown type: {value['type']}")

    return create_model("PropertiesSchema", **properties_schema)


def generate_dynamic_result_schema(properties_schema: Type[PropertiesSchema]):
    defaults = DefaultSettingsSchema(alias="properties", title="properties")
    return create_model("NotionDatabaseResponseSchema", __base__=NotionDatabaseResponseSchema, properties=(properties_schema, defaults.dict()))
