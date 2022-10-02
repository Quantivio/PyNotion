from typing import Any, Optional

import pydantic


class AuthoredBySchema(pydantic.BaseModel):
    object: str
    id: str


class ParentSchema(pydantic.BaseModel):
    type: str
    database_id: Optional[str]


class ResultSchema(pydantic.BaseModel):
    object: str
    id: str
    created_time: str
    last_edited_time: str
    created_by: AuthoredBySchema
    last_edited_by: AuthoredBySchema
    cover: Optional[Any]
    icon: Optional[Any]
    parent: ParentSchema
    properties: Any
    archived: bool
