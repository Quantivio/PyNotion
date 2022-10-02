from typing import List

from pynotionclient.schema.database import IdTypeSchema, ContentSchema


class RichTextSchema(IdTypeSchema):
    rich_text: List[ContentSchema]
