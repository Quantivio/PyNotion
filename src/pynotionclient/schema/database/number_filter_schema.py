from typing import Optional

from pynotionclient.schema.database.common_filter_schema import EqualsFilter, EmptyFilter


class NumberFilter(EqualsFilter, EmptyFilter):
    greater_than: Optional[int]
    greater_than_or_equal_to: Optional[int]
    less_than: Optional[int]
    less_than_or_equal_to: Optional[int]
