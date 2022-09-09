from typing import List

import pydantic

from schema.response.common_info_schema import IdTypeSchema, IdTypeNameSchema


class PersonEmailSchema(pydantic.BaseModel):
    email: str


class PersonItemSchema(IdTypeNameSchema):
    object: str
    avatar_url: str
    person: PersonEmailSchema


class PersonSchema(IdTypeSchema):
    people: List[PersonItemSchema]
