from typing import Optional

import pydantic


class EquationSchema(pydantic.BaseModel):
    expression: Optional[str]
