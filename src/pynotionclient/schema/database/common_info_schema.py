from typing import Optional

import pydantic


class IDSchema(pydantic.BaseModel):
    id: Optional[str]


class IdTypeSchema(IDSchema):
    type: Optional[str]


class IdNameSchema(IDSchema):
    name: str


class IdTypeNameSchema(IDSchema):
    type: str
    name: str
