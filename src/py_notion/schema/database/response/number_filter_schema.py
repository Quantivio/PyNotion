from .common_filter_schema import EmptyFilter, EqualsFilter


class NumberFilter(EqualsFilter, EmptyFilter):
	greater_than: int | None
	greater_than_or_equal_to: int | None
	less_than: int | None
	less_than_or_equal_to: int | None
