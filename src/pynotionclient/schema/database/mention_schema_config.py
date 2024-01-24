from typing import Optional

import pydantic

from pynotionclient.schema.database.response.common_info_schema import IDSchema
from pynotionclient.schema.database.response.person_schema import PersonEmailSchema


class UserSchemaConfig(pydantic.BaseModel):
    id: Optional[str]
    name: Optional[str]
    object: Optional[str]
    avatar_url: Optional[str]
    person: Optional[PersonEmailSchema]


class DatabaseSchemaConfig(pydantic.BaseModel):
    database: Optional[IDSchema]


class PageSchemaConfig(pydantic.BaseModel):
    page: Optional[IDSchema]


class UserIDSchemaConfig(pydantic.BaseModel):
    user: Optional[IDSchema]


# User, Page, database mention schema
class UPDMentionSchemaConfigConfigConfig(PageSchemaConfig, DatabaseSchemaConfig, UserSchemaConfig, UserIDSchemaConfig):
    pass
