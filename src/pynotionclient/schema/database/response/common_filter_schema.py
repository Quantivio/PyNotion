from typing import Optional

import pydantic


class EqualsFilter(pydantic.BaseModel):
    equals: Optional[str | bool | int] = None
    does_not_equals: Optional[str | bool | int] = None


class ContainsFilter(pydantic.BaseModel):
    contains: Optional[str] = None
    does_not_contain: Optional[str] = None


class EmptyFilter(pydantic.BaseModel):
    is_empty: Optional[bool] = None
    is_not_empty: Optional[bool] = None
