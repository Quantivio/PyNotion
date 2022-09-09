from typing import List

from schema.response.common_info_schema import IdTypeSchema, IdNameSchema


class MultiSelectItemSchema(IdNameSchema):
    id: str
    name: str
    color: str


class MultiSelectSchema(IdTypeSchema):
    id: str
    type: str
    multi_select: List[MultiSelectItemSchema]
