import pydantic

from .common_info_schema import IdTypeNameSchema, IdTypeSchema


class PersonEmailSchema(pydantic.BaseModel):
	email: str


class PersonItemSchema(IdTypeNameSchema):
	object: str
	avatar_url: str
	person: PersonEmailSchema


class PersonSchema(IdTypeSchema):
	people: list[PersonItemSchema]
