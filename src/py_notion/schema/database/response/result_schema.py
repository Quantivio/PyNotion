from typing import Any

import pydantic


class AuthoredBySchema(pydantic.BaseModel):
	object: str
	id: str


class ParentSchema(pydantic.BaseModel):
	type: str
	database_id: str | None = None


class ResultSchema(pydantic.BaseModel):
	object: str
	id: str
	created_time: str
	last_edited_time: str
	created_by: AuthoredBySchema
	last_edited_by: AuthoredBySchema
	cover: Any | None = None
	icon: Any | None = None
	parent: ParentSchema
	properties: Any = None
	archived: bool
