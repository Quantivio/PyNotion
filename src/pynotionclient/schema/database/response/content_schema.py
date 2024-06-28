from typing import Any, Optional

import pydantic

from pynotionclient.schema.database.annotations_schema_config import AnnotationsSchemaConfig
from pynotionclient.schema.database.equation_schema_config import EquationSchemaConfig
from pynotionclient.schema.database.mention_schema_config import UPDMentionSchemaConfigConfigConfig


class TextSchema(pydantic.BaseModel):
    content: str
    link: Any = None


class ContentSchema(pydantic.BaseModel):
    type: Optional[str] = None
    text: Optional[TextSchema] = None
    mention: Optional[UPDMentionSchemaConfigConfigConfig] = None
    annotations: Optional[AnnotationsSchemaConfig] = None
    equation: Optional[EquationSchemaConfig] = None
    plain_text: str
    href: Any = None
