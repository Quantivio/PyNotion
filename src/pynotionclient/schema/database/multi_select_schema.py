from typing import List

from pynotionclient.schema.database.common_info_schema import IdNameSchema, IdTypeSchema


class MultiSelectItemSchema(IdNameSchema):
    color: str


class MultiSelectSchema(IdTypeSchema):
    multi_select: List[MultiSelectItemSchema]
