from pynotionclient.schema.database import IdNameSchema, IdTypeSchema


class InternalStatusSchema(IdNameSchema):
    color: str


class StatusSchema(IdTypeSchema):
    status: InternalStatusSchema
