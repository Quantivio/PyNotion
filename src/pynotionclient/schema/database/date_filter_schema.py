from typing import Optional

from pynotionclient.schema.database import EmptyFilter, EqualsFilter


class DateFilter(EqualsFilter, EmptyFilter):
    before: Optional[str]
    after: Optional[str]
    on_or_before: Optional[str]
    on_or_after: Optional[str]
    past_week: Optional[dict]
    past_month: Optional[dict]
    past_year: Optional[dict]
    next_week: Optional[dict]
    next_month: Optional[dict]
    next_year: Optional[dict]
