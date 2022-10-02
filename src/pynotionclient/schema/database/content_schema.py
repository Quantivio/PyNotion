from typing import Optional, Any

import pydantic

from src.pynotionclient.schema.database.annotations_schema import AnnotationsSchema
from src.pynotionclient.schema.database.mention_schema import UPDMentionSchema


class TextSchema(pydantic.BaseModel):
    content: str
    link: Any


class ContentSchema(pydantic.BaseModel):
    type: str
    text: Optional[TextSchema]
    mention: Optional[UPDMentionSchema]
    annotations: AnnotationsSchema
    plain_text: str
    href: Any
