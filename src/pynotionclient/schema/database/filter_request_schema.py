from typing import Optional, List

import pydantic
from pydantic import Field

from pynotionclient.schema.database import DateFilter
from pynotionclient.schema.database import NumberFilter
from pynotionclient.schema.database import (
    CheckboxFilter,
    SelectFilter,
    MultiSelectFilter,
    PeopleFilter,
    FileFilter,
    RelationFilter,
)
from pynotionclient.schema.database import RichTextFilter
from pynotionclient.schema.database import TimeStampFilter


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
