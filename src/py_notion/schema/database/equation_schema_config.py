import pydantic


class EquationSchemaConfig(pydantic.BaseModel):
	expression: str | None = None
