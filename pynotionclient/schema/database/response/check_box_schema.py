from pynotionclient.schema.database.response.common_info_schema import IdTypeSchema


class CheckboxSchema(IdTypeSchema):
    checkbox: bool
