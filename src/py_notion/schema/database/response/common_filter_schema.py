import pydantic


class EqualsFilter(pydantic.BaseModel):
	equals: str | bool | int | None = None
	does_not_equals: str | bool | int | None = None


class ContainsFilter(pydantic.BaseModel):
	contains: str | None = None
	does_not_contain: str | None = None


class EmptyFilter(pydantic.BaseModel):
	is_empty: bool | None = None
	is_not_empty: bool | None = None
