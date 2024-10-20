from .common_filter_schema import ContainsFilter, EmptyFilter, EqualsFilter


class RichTextFilter(ContainsFilter, EqualsFilter, EmptyFilter):
	starts_with: str | None = None
	ends_with: str | None = None
