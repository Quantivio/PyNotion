from typing import List

import pydantic

from pynotionclient.schema.database.common_info_schema import IdTypeNameSchema, IdTypeSchema


class PersonEmailSchema(pydantic.BaseModel):
    email: str


class PersonItemSchema(IdTypeNameSchema):
    object: str
    avatar_url: str
    person: PersonEmailSchema


class PersonSchema(IdTypeSchema):
    people: List[PersonItemSchema]
