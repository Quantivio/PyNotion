from .common_info_schema import IdTypeSchema
from .content_schema import ContentSchema


class RichTextSchema(IdTypeSchema):
	rich_text: list[ContentSchema]
