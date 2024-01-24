from typing import Optional

from pynotionclient.schema.database.response.common_filter_schema import (
    EmptyFilter,
    EqualsFilter,
)


class NumberFilter(EqualsFilter, EmptyFilter):
    greater_than: Optional[int]
    greater_than_or_equal_to: Optional[int]
    less_than: Optional[int]
    less_than_or_equal_to: Optional[int]
