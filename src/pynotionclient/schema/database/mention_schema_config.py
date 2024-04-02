from typing import Optional

import pydantic
from pynotionclient.schema.database.response.common_info_schema import IDSchema
from pynotionclient.schema.database.response.person_schema import PersonEmailSchema


class UserSchemaConfig(pydantic.BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    object: Optional[str] = None
    avatar_url: Optional[str] = None
    person: Optional[PersonEmailSchema] = None


class DatabaseSchemaConfig(pydantic.BaseModel):
    database: Optional[IDSchema] = None


class PageSchemaConfig(pydantic.BaseModel):
    page: Optional[IDSchema] = None


class UserIDSchemaConfig(pydantic.BaseModel):
    user: Optional[IDSchema] = None


# User, Page, database mention schema
class UPDMentionSchemaConfigConfigConfig(PageSchemaConfig, DatabaseSchemaConfig, UserSchemaConfig, UserIDSchemaConfig):
    pass
