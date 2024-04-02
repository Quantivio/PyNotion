import pydantic
from pynotionclient.schema.database.response.content_schema import ContentSchema


class TitleSchema(pydantic.BaseModel):
    title: list[ContentSchema]
