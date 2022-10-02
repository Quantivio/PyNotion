from pynotionclient.schema.database import IdTypeSchema


class CheckboxSchema(IdTypeSchema):
    checkbox: bool
