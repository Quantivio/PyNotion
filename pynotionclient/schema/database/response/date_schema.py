from typing import Any

import pydantic

from pynotionclient.schema.database.response.common_info_schema import IdTypeSchema


class InternalDateSchema(pydantic.BaseModel):
    start: str
    end: Any = None
    time_zone: Any = None


class DateSchema(IdTypeSchema):
    date: InternalDateSchema
