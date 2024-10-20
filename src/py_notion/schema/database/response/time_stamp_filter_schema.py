from typing import Any

import pydantic


class TimeStampFilter(pydantic.BaseModel):
	timestamp: str
	created_time: Any | None = None
	last_edited_time: Any | None = None
