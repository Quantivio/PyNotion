import pydantic

from .response.common_info_schema import IDSchema
from .response.person_schema import PersonEmailSchema


class UserSchemaConfig(pydantic.BaseModel):
	id: str | None = None
	name: str | None = None
	object: str | None = None
	avatar_url: str | None = None
	person: PersonEmailSchema | None = None


class DatabaseSchemaConfig(pydantic.BaseModel):
	database: IDSchema | None = None


class PageSchemaConfig(pydantic.BaseModel):
	page: IDSchema | None = None


class UserIDSchemaConfig(pydantic.BaseModel):
	user: IDSchema | None = None


# User, Page, database mention schema
class UPDMentionSchemaConfigConfigConfig(PageSchemaConfig, DatabaseSchemaConfig, UserSchemaConfig, UserIDSchemaConfig):
	pass
