from typing import List

from schema.response.common_info_schema import IdTypeSchema
from schema.response.content_schema import ContentSchema


class RichTextSchema(IdTypeSchema):
    rich_text: List[ContentSchema]
