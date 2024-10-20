from py_notion.schema.database import ContentSchema

from .common_info_schema import IdTypeSchema


class RichTextSchema(IdTypeSchema):
	rich_text: list[ContentSchema]
