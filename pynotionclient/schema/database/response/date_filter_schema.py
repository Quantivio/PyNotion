from typing import Any, Optional

from pynotionclient.schema.database.response.common_filter_schema import EmptyFilter, EqualsFilter


class DateFilter(EqualsFilter, EmptyFilter):
    before: Optional[str] = None
    after: Optional[str] = None
    on_or_before: Optional[str] = None
    on_or_after: Optional[str] = None
    past_week: Optional[dict[str, Any]] = None
    past_month: Optional[dict[str, Any]] = None
    past_year: Optional[dict[str, Any]] = None
    next_week: Optional[dict[str, Any]] = None
    next_month: Optional[dict[str, Any]] = None
    next_year: Optional[dict[str, Any]] = None
