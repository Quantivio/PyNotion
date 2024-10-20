from typing import Any

import pydantic
from pydantic import Field

from .date_filter_schema import DateFilter
from .number_filter_schema import NumberFilter
from .other_filters_schema import (
	CheckboxFilter,
	FileFilter,
	MultiSelectFilter,
	PeopleFilter,
	RelationFilter,
	SelectFilter,
)
from .rich_text_filter_schema import RichTextFilter
from .time_stamp_filter_schema import TimeStampFilter


class PropertyFilter(pydantic.BaseModel):
	property: str
	rich_text: RichTextFilter | None = None
	number: NumberFilter | None = None
	checkbox: CheckboxFilter | None = None
	select: SelectFilter | None = None
	multi_select: MultiSelectFilter | None = None
	date: DateFilter | None = None
	people: PeopleFilter | None = None
	file: FileFilter | None = None
	relation: RelationFilter | None = None


class CompoundFilterOR(pydantic.BaseModel):
	or_filter: list[PropertyFilter] | None = Field(
		None,
		alias="or",
		title="or",
		description="OR compound logical filter operator to pass multiple filter as list",
	)


class CompoundFilterAND(pydantic.BaseModel):
	and_filter: list[PropertyFilter] | None = Field(
		None,
		alias="and",
		title="and",
		description="AND compound logical filter operator to pass multiple filter as list",
	)


class Filter(pydantic.BaseModel):
	page_size: int
	filter: PropertyFilter | TimeStampFilter | CompoundFilterOR | CompoundFilterAND | dict[str, Any] | None = None
