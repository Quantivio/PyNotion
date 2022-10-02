from typing import Optional, Any

import pydantic
from pydantic import validator

from pynotionclient.schema.database.annotations_schema import AnnotationsSchema
from pynotionclient.schema.database.equation_schema import EquationSchema
from pynotionclient.schema.database.mention_schema import UPDMentionSchema


class TextSchema(pydantic.BaseModel):
    content: str
    link: Any


class ContentSchema(pydantic.BaseModel):
    type: Optional[str]
    text: Optional[TextSchema]
    mention: Optional[UPDMentionSchema]
    annotations: Optional[AnnotationsSchema]
    equation: Optional[EquationSchema]
    plain_text: str
    href: Any

    @validator("type")
    def validate_type(cls, content_type):
        if content_type not in ["text", "mention", "equation"]:
            raise ValueError("Content type must be text, mention, or equation")
