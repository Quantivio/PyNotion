from typing import List

import pydantic

from pynotionclient.schema.database.content_schema import ContentSchema


class TitleSchema(pydantic.BaseModel):
    title: List[ContentSchema]
