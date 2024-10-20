from typing import Any

import pydantic

from .common_info_schema import IdTypeSchema


class InternalDateSchema(pydantic.BaseModel):
	start: str
	end: Any = None
	time_zone: Any = None


class DateSchema(IdTypeSchema):
	date: InternalDateSchema
