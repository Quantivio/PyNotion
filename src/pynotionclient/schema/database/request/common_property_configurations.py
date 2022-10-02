import pydantic


class TitleConfiguration(pydantic.BaseModel):
    title: dict = {}


class RichTextConfiguration(pydantic.BaseModel):
    rich_text: dict = {}


class CheckboxConfiguration(pydantic.BaseModel):
    checkbox: dict = {}


class DateConfiguration(pydantic.BaseModel):
    date: dict = {}


class PeopleConfiguration(pydantic.BaseModel):
    people: dict = {}


class FileConfiguration(pydantic.BaseModel):
    file: dict = {}


class UrlConfiguration(pydantic.BaseModel):
    url: dict = {}


class EmailConfiguration(pydantic.BaseModel):
    email: dict = {}


class PhoneNumberConfiguration(pydantic.BaseModel):
    phone_number: dict = {}


class CreatedTimeConfiguration(pydantic.BaseModel):
    created_time: dict = {}


class CreatedByConfiguration(pydantic.BaseModel):
    created_by: dict = {}


class LastEditedTimeConfiguration(pydantic.BaseModel):
    last_edited_time: dict = {}


class LastEditedByConfiguration(pydantic.BaseModel):
    last_edited_by: dict = {}


# TODO: Add forumula, rollup, and relation
