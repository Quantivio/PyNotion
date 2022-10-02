from pynotionclient.schema.database.common_info_schema import IdTypeSchema


class CheckboxSchema(IdTypeSchema):
    checkbox: bool
