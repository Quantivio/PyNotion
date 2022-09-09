from typing import List

from schema.response.ContentSchema import ContentSchema
from schema.response.common_info_schema import IdTypeSchema


class RichTextSchema(IdTypeSchema):
    rich_text: List[ContentSchema]
