from typing import Any

import pydantic

from pynotionclient.schema.database import IdTypeSchema


class InternalDateSchema(pydantic.BaseModel):
    start: str
    end: Any
    time_zone: Any


class DateSchema(IdTypeSchema):
    date: InternalDateSchema
