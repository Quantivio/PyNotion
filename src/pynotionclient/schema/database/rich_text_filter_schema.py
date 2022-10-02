from typing import Optional

from src.pynotionclient.schema.database import ContainsFilter, EqualsFilter, EmptyFilter


class RichTextFilter(ContainsFilter, EqualsFilter, EmptyFilter):
    starts_with: Optional[str]
    ends_with: Optional[str]
