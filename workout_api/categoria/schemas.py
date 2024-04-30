from typing import Annotated

from pydantic import UUID4, Field

from workout_api.contrib.schemas import BaseSchemas


class CategoriaIn(BaseSchemas):
    nome: Annotated[str, Field(max_length=50)]

class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]