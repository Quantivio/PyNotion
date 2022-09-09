from typing import Any

import pydantic

from schema.response.common_info_schema import IdTypeSchema


class InternalDateSchema(pydantic.BaseModel):
    start: str
    end: Any
    time_zone: Any


class DateSchema(IdTypeSchema):
    date: InternalDateSchema
