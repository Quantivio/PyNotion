from typing import Any

import pydantic
from pydantic import field_validator

from src.py_notion.schema.database.annotations_schema_config import AnnotationsSchemaConfig
from src.py_notion.schema.database.equation_schema_config import EquationSchemaConfig
from src.py_notion.schema.database.mention_schema_config import UPDMentionSchemaConfigConfigConfig


class TextConfiguration(pydantic.BaseModel):
	content: str
	link: str | None = None


class ContentConfiguration(pydantic.BaseModel):
	type: str | None = None
	text: TextConfiguration | None = None
	mention: UPDMentionSchemaConfigConfigConfig | None = None
	annotations: AnnotationsSchemaConfig | None = None
	equation: EquationSchemaConfig | None = None
	plain_text: str
	href: Any = None

	@classmethod
	@field_validator("type")
	def validate_type(cls, content_type: str):  # type: ignore
		if content_type not in ["text", "mention", "equation"]:
			value_error: str = "Content type must be text, mention, or equation"
			raise ValueError(value_error)
