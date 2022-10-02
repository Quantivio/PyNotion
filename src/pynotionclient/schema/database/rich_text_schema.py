from typing import List

from src.pynotionclient.schema.database import IdTypeSchema, ContentSchema


class RichTextSchema(IdTypeSchema):
    rich_text: List[ContentSchema]
