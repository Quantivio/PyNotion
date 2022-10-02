from typing import Optional

from pynotionclient.schema.database.common_filter_schema import ContainsFilter, EqualsFilter, EmptyFilter


class RichTextFilter(ContainsFilter, EqualsFilter, EmptyFilter):
    starts_with: Optional[str]
    ends_with: Optional[str]
