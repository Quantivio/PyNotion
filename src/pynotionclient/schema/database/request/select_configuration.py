import pydantic


class SelectOptionsConfiguration(pydantic.BaseModel):
    name: str
    color: str


class SelecOptionsListConfig(pydantic.BaseModel):
    options: list[SelectOptionsConfiguration]


class SelectConfiguration(pydantic.BaseModel):
    select: SelecOptionsListConfig


class MultiSelectConfiguration(pydantic.BaseModel):
    multi_select: SelecOptionsListConfig
