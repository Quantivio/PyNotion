from pynotionclient.schema.database.response.common_info_schema import IdTypeSchema
from pynotionclient.schema.database.response.content_schema import ContentSchema


class RichTextSchema(IdTypeSchema):
    rich_text: list[ContentSchema]
