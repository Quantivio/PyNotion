from typing import List

from schema.response.content_schema import ContentSchema
from schema.response.common_info_schema import IdTypeSchema


class RichTextSchema(IdTypeSchema):
    rich_text: List[ContentSchema]
