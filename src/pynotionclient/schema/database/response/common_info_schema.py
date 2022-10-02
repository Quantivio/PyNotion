import pydantic


class IDSchema(pydantic.BaseModel):
    id: str


class IdTypeSchema(IDSchema):
    type: str


class IdNameSchema(IDSchema):
    name: str


class IdTypeNameSchema(IDSchema):
    type: str
    name: str
