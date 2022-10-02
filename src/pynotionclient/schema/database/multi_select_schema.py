from typing import List

from src.pynotionclient.schema.database import IdNameSchema, IdTypeSchema


class MultiSelectItemSchema(IdNameSchema):
    color: str


class MultiSelectSchema(IdTypeSchema):
    multi_select: List[MultiSelectItemSchema]
