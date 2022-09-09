from schema.response.common_info_schema import IdTypeSchema, IdNameSchema


class InternalStatusSchema(IdNameSchema):
    color: str


class StatusSchema(IdTypeSchema):
    status: InternalStatusSchema
