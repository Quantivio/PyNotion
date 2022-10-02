from typing import List

from src.pynotionclient.schema import IdNameSchema, IdTypeSchema


class MultiSelectItemSchema(IdNameSchema):
    color: str


class MultiSelectSchema(IdTypeSchema):
    multi_select: List[MultiSelectItemSchema]
