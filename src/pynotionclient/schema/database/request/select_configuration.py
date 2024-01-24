import pydantic


class SelectOptionsConfiguration(pydantic.BaseModel):
    name: str
    color: str


class SelectOptionsListConfig(pydantic.BaseModel):
    options: list[SelectOptionsConfiguration]


class SelectConfiguration(pydantic.BaseModel):
    select: SelectOptionsListConfig


class MultiSelectConfiguration(pydantic.BaseModel):
    multi_select: SelectOptionsListConfig
