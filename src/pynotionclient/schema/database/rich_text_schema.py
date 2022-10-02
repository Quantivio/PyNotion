from typing import List

from pynotionclient.schema.database.common_info_schema import IdTypeSchema
from pynotionclient.schema.database.content_schema import ContentSchema


class RichTextSchema(IdTypeSchema):
    rich_text: List[ContentSchema]
