import pydantic

from .content_schema import ContentSchema


class TitleSchema(pydantic.BaseModel):
	title: list[ContentSchema]
