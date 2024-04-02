from typing import Any, Optional

import pydantic


class TimeStampFilter(pydantic.BaseModel):
    timestamp: str
    created_time: Optional[Any] = None
    last_edited_time: Optional[Any] = None
