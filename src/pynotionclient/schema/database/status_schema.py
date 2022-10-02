from pynotionclient.schema.database.common_info_schema import IdNameSchema, IdTypeSchema


class InternalStatusSchema(IdNameSchema):
    color: str


class StatusSchema(IdTypeSchema):
    status: InternalStatusSchema
