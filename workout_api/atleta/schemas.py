from typing import Annotated, Optional

from pydantic import BaseModel, Field, PositiveFloat

from workout_api.categoria.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchemas, OutMixin


class Atleta(BaseSchemas):
    nome: Annotated[str, Field(max_length=50)]
    cpf: Annotated[str, Field(max_length=11)]
    idade: Annotated[int, Field()]
    peso: Annotated[PositiveFloat, Field()]
    altura: Annotated[PositiveFloat, Field()]
    sexo: Annotated[str, Field(max_length=1)]
    categoria: Annotated[CategoriaIn, Field()]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field()]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchemas):
    nome: Annotated[Optional[str], Field(None, max_length=50)]
    idade: Annotated[Optional[int], Field(None)]