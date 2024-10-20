from typing import Any

from src.py_notion.schema.database.response.common_filter_schema import EmptyFilter, EqualsFilter


class DateFilter(EqualsFilter, EmptyFilter):
	before: str | None = None
	after: str | None = None
	on_or_before: str | None = None
	on_or_after: str | None = None
	past_week: dict[str, Any] | None = None
	past_month: dict[str, Any] | None = None
	past_year: dict[str, Any] | None = None
	next_week: dict[str, Any] | None = None
	next_month: dict[str, Any] | None = None
	next_year: dict[str, Any] | None = None
