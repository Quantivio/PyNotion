from .common_info_schema import IdNameSchema, IdTypeSchema


class InternalSelectSchema(IdNameSchema):
	color: str


class SelectSchema(IdTypeSchema):
	select: InternalSelectSchema
