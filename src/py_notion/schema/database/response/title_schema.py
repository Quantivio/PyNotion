import pydantic
from py_notion.schema.database import ContentSchema


class TitleSchema(pydantic.BaseModel):
	title: list[ContentSchema]
