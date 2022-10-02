from typing import List

import pydantic

from src.pynotionclient.schema import ContentSchema


class TitleSchema(pydantic.BaseModel):
    title: List[ContentSchema]
