from pydantic import BaseModel


class TitleConfiguration(BaseModel):
    title: dict = {}


class RichTextConfiguration(BaseModel):
    rich_text: dict = {}


class CheckboxConfiguration(BaseModel):
    checkbox: dict = {}


class DateConfiguration(BaseModel):
    date: dict = {}


class PeopleConfiguration(BaseModel):
    people: dict = {}


class FileConfiguration(BaseModel):
    file: dict = {}


class UrlConfiguration(BaseModel):
    url: dict = {}


class EmailConfiguration(BaseModel):
    email: dict = {}


class PhoneNumberConfiguration(BaseModel):
    phone_number: dict = {}


class CreatedTimeConfiguration(BaseModel):
    created_time: dict = {}


class CreatedByConfiguration(BaseModel):
    created_by: dict = {}


class LastEditedTimeConfiguration(BaseModel):
    last_edited_time: dict = {}


class LastEditedByConfiguration(BaseModel):
    last_edited_by: dict = {}


# TODO: Add formula, rollup, and relation
