from pynotionclient.schema.database.response.common_info_schema import (
    IdNameSchema,
    IdTypeSchema,
)


class MultiSelectItemSchema(IdNameSchema):
    color: str


class MultiSelectSchema(IdTypeSchema):
    multi_select: list[MultiSelectItemSchema]
