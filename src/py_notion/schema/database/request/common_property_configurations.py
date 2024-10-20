from typing import Any

from pydantic import BaseModel


class TitleConfiguration(BaseModel):
	title: dict[str, Any] = {}


class RichTextConfiguration(BaseModel):
	rich_text: dict[str, Any] = {}


class CheckboxConfiguration(BaseModel):
	checkbox: dict[str, Any] = {}


class DateConfiguration(BaseModel):
	date: dict[str, Any] = {}


class PeopleConfiguration(BaseModel):
	people: dict[str, Any] = {}


class FileConfiguration(BaseModel):
	file: dict[str, Any] = {}


class UrlConfiguration(BaseModel):
	url: dict[str, Any] = {}


class EmailConfiguration(BaseModel):
	email: dict[str, Any] = {}


class PhoneNumberConfiguration(BaseModel):
	phone_number: dict[str, Any] = {}


class CreatedTimeConfiguration(BaseModel):
	created_time: dict[str, Any] = {}


class CreatedByConfiguration(BaseModel):
	created_by: dict[str, Any] = {}


class LastEditedTimeConfiguration(BaseModel):
	last_edited_time: dict[str, Any] = {}


class LastEditedByConfiguration(BaseModel):
	last_edited_by: dict[str, Any] = {}


# TODO: Add formula, rollup, and relation
