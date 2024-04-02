from typing import Any, Optional

import pydantic


class AuthoredBySchema(pydantic.BaseModel):
    object: str
    id: str


class ParentSchema(pydantic.BaseModel):
    type: str
    database_id: Optional[str] = None


class ResultSchema(pydantic.BaseModel):
    object: str
    id: str
    created_time: str
    last_edited_time: str
    created_by: AuthoredBySchema
    last_edited_by: AuthoredBySchema
    cover: Optional[Any] = None
    icon: Optional[Any] = None
    parent: ParentSchema
    properties: Any = None
    archived: bool
