import pydantic


class AnnotationsSchemaConfig(pydantic.BaseModel):
	bold: bool
	italic: bool
	strikethrough: bool
	underline: bool
	code: bool
	color: str
