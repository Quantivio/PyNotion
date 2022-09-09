from typing import List

import pydantic

from schema.response.content_schema import ContentSchema


class TitleSchema(pydantic.BaseModel):
    title: List[ContentSchema]