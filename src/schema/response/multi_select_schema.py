from typing import List

from schema.response.common_info_schema import IdTypeSchema, IdNameSchema


class MultiSelectItemSchema(IdNameSchema):
    color: str


class MultiSelectSchema(IdTypeSchema):
    multi_select: List[MultiSelectItemSchema]
