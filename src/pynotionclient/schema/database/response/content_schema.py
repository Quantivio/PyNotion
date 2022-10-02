from typing import Optional, Any

import pydantic

from pynotionclient.schema.database.annotations_schema_config import (
    AnnotationsSchemaConfig,
)
from pynotionclient.schema.database.equation_schema_config import EquationSchemaConfig
from pynotionclient.schema.database.mention_schema_config import (
    UPDMentionSchemaConfigConfigConfig,
)


class TextSchema(pydantic.BaseModel):
    content: str
    link: Any


class ContentSchema(pydantic.BaseModel):
    type: Optional[str]
    text: Optional[TextSchema]
    mention: Optional[UPDMentionSchemaConfigConfigConfig]
    annotations: Optional[AnnotationsSchemaConfig]
    equation: Optional[EquationSchemaConfig]
    plain_text: str
    href: Any
