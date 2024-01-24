from typing import Any, Optional

import pydantic
from pydantic import field_validator

from pynotionclient.schema.database.annotations_schema_config import (
    AnnotationsSchemaConfig,
)
from pynotionclient.schema.database.equation_schema_config import EquationSchemaConfig
from pynotionclient.schema.database.mention_schema_config import (
    UPDMentionSchemaConfigConfigConfig,
)


class TextConfiguration(pydantic.BaseModel):
    content: str
    link: Optional[str]


class ContentConfiguration(pydantic.BaseModel):
    type: Optional[str]
    text: Optional[TextConfiguration]
    mention: Optional[UPDMentionSchemaConfigConfigConfig]
    annotations: Optional[AnnotationsSchemaConfig]
    equation: Optional[EquationSchemaConfig]
    plain_text: str
    href: Any

    @field_validator("type")
    def validate_type(cls, content_type):  # noqa
        if content_type not in ["text", "mention", "equation"]:
            raise ValueError("Content type must be text, mention, or equation")
