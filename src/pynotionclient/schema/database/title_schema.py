from typing import List

import pydantic

from src.pynotionclient.schema.database import ContentSchema


class TitleSchema(pydantic.BaseModel):
    title: List[ContentSchema]
