from schema.response.common_info_schema import IdTypeSchema


class CheckboxSchema(IdTypeSchema):
    id: str
    type: str
    checkbox: bool
