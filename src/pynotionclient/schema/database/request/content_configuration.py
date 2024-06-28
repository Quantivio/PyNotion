from typing import Any, Optional

import pydantic
from pydantic import field_validator

from pynotionclient.schema.database.annotations_schema_config import AnnotationsSchemaConfig
from pynotionclient.schema.database.equation_schema_config import EquationSchemaConfig
from pynotionclient.schema.database.mention_schema_config import UPDMentionSchemaConfigConfigConfig


class TextConfiguration(pydantic.BaseModel):
    content: str
    link: Optional[str] = None


class ContentConfiguration(pydantic.BaseModel):
    type: Optional[str] = None
    text: Optional[TextConfiguration] = None
    mention: Optional[UPDMentionSchemaConfigConfigConfig] = None
    annotations: Optional[AnnotationsSchemaConfig] = None
    equation: Optional[EquationSchemaConfig] = None
    plain_text: str
    href: Any = None

    @field_validator("type")
    @classmethod
    def validate_type(cls, content_type: str):  # type: ignore
        if content_type not in ["text", "mention", "equation"]:
            raise ValueError("Content type must be text, mention, or equation")
