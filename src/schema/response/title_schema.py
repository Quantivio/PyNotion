from typing import List

import pydantic

from schema.response.ContentSchema import ContentSchema


class TitleSchema(pydantic.BaseModel):
    title: List[ContentSchema]