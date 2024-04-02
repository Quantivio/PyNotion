from typing import Optional

import pydantic
from pydantic import Field

from pynotionclient.schema.database.response.date_filter_schema import DateFilter
from pynotionclient.schema.database.response.number_filter_schema import NumberFilter
from pynotionclient.schema.database.response.other_filters_schema import (
    CheckboxFilter,
    FileFilter,
    MultiSelectFilter,
    PeopleFilter,
    RelationFilter,
    SelectFilter,
)
from pynotionclient.schema.database.response.rich_text_filter_schema import (
    RichTextFilter,
)
from pynotionclient.schema.database.response.time_stamp_filter_schema import (
    TimeStampFilter,
)


class PropertyFilter(pydantic.BaseModel):
    property: str
    rich_text: Optional[RichTextFilter] = None
    number: Optional[NumberFilter] = None
    checkbox: Optional[CheckboxFilter] = None
    select: Optional[SelectFilter] = None
    multi_select: Optional[MultiSelectFilter] = None
    date: Optional[DateFilter] = None
    people: Optional[PeopleFilter] = None
    file: Optional[FileFilter] = None
    relation: Optional[RelationFilter] = None


class CompoundFilterOR(pydantic.BaseModel):
    or_filter: Optional[list[PropertyFilter]] = Field(
        None, alias="or",
        title="or",
        description="OR compound logical filter operator to pass multiple filter as list",
    )


class CompoundFilterAND(pydantic.BaseModel):
    and_filter: Optional[list[PropertyFilter]] = Field(
        None, alias="and",
        title="and",
        description="AND compound logical filter operator to pass multiple filter as list",
    )


class Filter(pydantic.BaseModel):
    page_size: int
    filter: Optional[PropertyFilter | TimeStampFilter | CompoundFilterOR | CompoundFilterAND | dict] = None
