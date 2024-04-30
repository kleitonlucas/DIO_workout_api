from datetime import datetime
from typing import Annotated

from pydantic import UUID4, BaseModel, Field


class BaseSchemas(BaseModel):
    class config:
        extra = "forbid"
        from_attributes = True

class OutMixin(BaseSchemas):
    id: Annotated[UUID4, Field()]
    created_at: Annotated[datetime, Field()]