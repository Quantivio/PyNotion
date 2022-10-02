from typing import Optional

from src.pynotionclient.schema import ContainsFilter, EqualsFilter, EmptyFilter


class RichTextFilter(ContainsFilter, EqualsFilter, EmptyFilter):
    starts_with: Optional[str]
    ends_with: Optional[str]
