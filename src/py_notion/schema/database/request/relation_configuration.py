from enum import Enum

import pydantic


class DatabaseRelationTypes(str, Enum):
	SINGLE_PROPERTY = "single_property"
	DUAL_PROPERTY = "dual_property"


class RelationConfiguration(pydantic.BaseModel):
	type: DatabaseRelationTypes = DatabaseRelationTypes.SINGLE_PROPERTY
	database_id: str
