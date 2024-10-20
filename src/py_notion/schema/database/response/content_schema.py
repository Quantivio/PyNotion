from typing import Any

import pydantic

from src.py_notion.schema.database.annotations_schema_config import AnnotationsSchemaConfig
from src.py_notion.schema.database.equation_schema_config import EquationSchemaConfig
from src.py_notion.schema.database.mention_schema_config import UPDMentionSchemaConfigConfigConfig


class TextSchema(pydantic.BaseModel):
	content: str
	link: Any = None


class ContentSchema(pydantic.BaseModel):
	type: str | None = None
	text: TextSchema | None = None
	mention: UPDMentionSchemaConfigConfigConfig | None = None
	annotations: AnnotationsSchemaConfig | None = None
	equation: EquationSchemaConfig | None = None
	plain_text: str
	href: Any = None
