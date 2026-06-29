"""Schemas Pydantic da API de extracao de vagas.

Esta e a fonte da verdade do formato retornado pela aplicacao.
"""

from difflib import get_close_matches
from enum import Enum
import unicodedata
from typing import Any, List, Optional

from pydantic import BaseModel, Field, field_validator


def _null_texto_para_none(valor: Any) -> Any:
    if isinstance(valor, str) and valor.strip().lower() in {"", "null", "none"}:
        return None
    return valor


def _normalizar_texto(valor: str) -> str:
    sem_acentos = unicodedata.normalize("NFD", valor.strip().lower())
    sem_marcas = "".join(
        caractere
        for caractere in sem_acentos
        if unicodedata.category(caractere) != "Mn"
    )
    com_espacos = "".join(
        caractere if caractere.isalnum() else " "
        for caractere in sem_marcas
    )
    return " ".join(com_espacos.split())


def _normalizar_por_alias(
    valor: str,
    aliases: dict[str, str],
    cutoff: float = 0.8,
) -> str:
    chave = _normalizar_texto(valor)

    if chave in aliases:
        return aliases[chave]

    match = get_close_matches(chave, aliases.keys(), n=1, cutoff=cutoff)
    if match:
        return aliases[match[0]]

    return valor


class Modalidade(str, Enum):
    """Modalidade de trabalho declarada na vaga."""

    REMOTO = "remoto"
    HIBRIDO = "hibrido"
    PRESENCIAL = "presencial"


class Nivel(str, Enum):
    """Nivel de senioridade declarado na vaga."""

    ESTAGIO = "estagio"
    JUNIOR = "junior"
    PLENO = "pleno"
    SENIOR = "senior"


class Salario(BaseModel):
    """Faixa salarial da vaga."""

    min: Optional[float] = None
    max: Optional[float] = None

    @field_validator("min", "max", mode="before")
    @classmethod
    def normalizar_null_texto(cls, valor: Any) -> Any:
        return _null_texto_para_none(valor)


class Vaga(BaseModel):
    """Estrutura final extraida de um anuncio de vaga."""

    cargo: str = Field(..., description="Cargo ou titulo da vaga")
    empresa: Optional[str] = None
    localidade: Optional[str] = None
    modalidade: Modalidade
    nivel: Optional[Nivel] = None
    salario: Optional[Salario] = None
    requisitos: List[str] = Field(default_factory=list)
    beneficios: List[str] = Field(default_factory=list)

    @field_validator("empresa", "localidade", "salario", mode="before")
    @classmethod
    def normalizar_campos_nulos(cls, valor: Any) -> Any:
        return _null_texto_para_none(valor)

    @field_validator("modalidade", mode="before")
    @classmethod
    def normalizar_modalidade(cls, valor: Any) -> Any:
        if not isinstance(valor, str):
            return valor

        aliases = {
            "remota": "remoto",
            "remoto": "remoto",
            "hibrida": "hibrido",
            "hibrido": "hibrido",
            "presencial": "presencial",
        }
        return _normalizar_por_alias(valor, aliases)

    @field_validator("nivel", mode="before")
    @classmethod
    def normalizar_nivel(cls, valor: Any) -> Any:
        valor = _null_texto_para_none(valor)
        if not isinstance(valor, str):
            return valor

        aliases = {
            "estagio": "estagio",
            "estagiario": "estagio",
            "junior": "junior",
            "jr": "junior",
            "pleno": "pleno",
            "senior": "senior",
            "sr": "senior",
        }
        return _normalizar_por_alias(valor, aliases)


class RequestExtracao(BaseModel):
    """Corpo do POST /extrair."""

    texto: str = Field(..., min_length=1, description="Texto bruto do anuncio")
