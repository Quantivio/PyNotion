from typing import Optional

import pydantic


class EquationSchemaConfig(pydantic.BaseModel):
    expression: Optional[str] = None
