from typing import Optional

import pydantic


class EqualsFilter(pydantic.BaseModel):
    equals: Optional[str | bool | int]
    does_not_equals: Optional[str | bool | int]


class ContainsFilter(pydantic.BaseModel):
    contains: Optional[str]
    does_not_contain: Optional[str]


class EmptyFilter(pydantic.BaseModel):
    is_empty: Optional[bool]
    is_not_empty: Optional[bool]
