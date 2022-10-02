from typing import Optional

import pydantic

from pynotionclient.schema.database import IDSchema, PersonEmailSchema


class UserSchema(pydantic.BaseModel):
    id: Optional[str]
    name: Optional[str]
    object: Optional[str]
    avatar_url: Optional[str]
    person: Optional[PersonEmailSchema]


class DatabaseSchema(pydantic.BaseModel):
    database: Optional[IDSchema]


class PageSchema(pydantic.BaseModel):
    page: Optional[IDSchema]


# User, Page, database mention schema
class UPDMentionSchema(PageSchema, DatabaseSchema, UserSchema):
    pass
