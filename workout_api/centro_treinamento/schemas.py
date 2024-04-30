from typing import Annotated

from pydantic import UUID4, Field

from workout_api.contrib.schemas import BaseSchemas


class CentroTreinamentoIn(BaseSchemas):
    nome: Annotated[str, Field(max_length=20)]
    endereco: Annotated[str, Field(max_length=60)]
    proprietario: Annotated[str, Field(max_length=30)]

class CentroTreinamentoAtleta(BaseSchemas):
    nome: Annotated[str, Field(max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do centro de treinamento')]