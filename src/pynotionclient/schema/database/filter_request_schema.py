from typing import Optional, List

import pydantic
from pydantic import Field

from src.pynotionclient.schema import DateFilter
from src.pynotionclient.schema import NumberFilter
from src.pynotionclient.schema import (
    CheckboxFilter,
    SelectFilter,
    MultiSelectFilter,
    PeopleFilter,
    FileFilter,
    RelationFilter,
)
from src.pynotionclient.schema import RichTextFilter
from src.pynotionclient.schema import TimeStampFilter


class PropertyFilter(pydantic.BaseModel):
    property: str
    rich_text: Optional[RichTextFilter]
    number: Optional[NumberFilter]
    checkbox: Optional[CheckboxFilter]
    select: Optional[SelectFilter]
    multi_select: Optional[MultiSelectFilter]
    date: Optional[DateFilter]
    people: Optional[PeopleFilter]
    file: Optional[FileFilter]
    relation: Optional[RelationFilter]


class CompoundFilterOR(pydantic.BaseModel):
    or_filter: Optional[List[PropertyFilter]] = Field(
        alias="or",
        title="or",
        description="OR compound logical filter operator to pass multiple filter as list",
    )


class CompoundFilterAND(pydantic.BaseModel):
    and_filter: Optional[List[PropertyFilter]] = Field(
        alias="and",
        title="and",
        description="AND compound logical filter operator to pass multiple filter as list",
    )


class Filter(pydantic.BaseModel):
    page_size: int
    filter: Optional[PropertyFilter | TimeStampFilter | CompoundFilterOR | CompoundFilterAND | dict] = None
