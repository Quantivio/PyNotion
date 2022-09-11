from typing import Any, Optional

import pydantic


class TimeStampFilter(pydantic.BaseModel):
    timestamp: str
    created_time: Optional[Any]
    last_edited_time: Optional[Any]
