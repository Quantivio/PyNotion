from typing import List

import pydantic

from pynotionclient.schema.database import ContentSchema


class TitleSchema(pydantic.BaseModel):
    title: List[ContentSchema]
