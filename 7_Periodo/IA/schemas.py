"""Schemas Pydantic da API de extração de vagas.

Esta é a fonte da verdade do formato. Tanto a API quanto o cliente Ollama
referenciam estas classes para garantir que estamos todos falando do mesmo
JSON.
"""
from enum import Enum
import unicodedata
from typing import Optional, List, Any
from pydantic import BaseModel, Field, field_validator


def _null_texto_para_none(valor: Any) -> Any:
    if isinstance(valor, str) and valor.strip().lower() in {"", "null", "none"}:
        return None
    return valor


def _normalizar_texto(valor: str) -> str:
    sem_acentos = unicodedata.normalize("NFD", valor.strip().lower())
    return "".join(
        caractere
        for caractere in sem_acentos
        if unicodedata.category(caractere) != "Mn"
    )


class Modalidade(str, Enum):
    """Modalidade de trabalho declarada na vaga."""
    REMOTO = "remoto"
    HIBRIDO = "hibrido"
    PRESENCIAL = "presencial"


class Nivel(str, Enum):
    """Nível de senioridade declarado na vaga."""
    ESTAGIO = "estagio"
    JUNIOR = "junior"
    PLENO = "pleno"
    SENIOR = "senior"


class Salario(BaseModel):
    """Faixa salarial. Ambos os campos são opcionais para acomodar vagas
    com apenas o mínimo, apenas o máximo, ou nenhum dos dois (caso de
    salário "a combinar" — neste caso, o objeto Salario inteiro deve ser
    None na Vaga)."""
    min: Optional[float] = None
    max: Optional[float] = None

    @field_validator("min", "max", mode="before")
    @classmethod
    def normalizar_null_texto(cls, valor: Any) -> Any:
        return _null_texto_para_none(valor)


class Vaga(BaseModel):
    """Estrutura final extraída de um anúncio de vaga.

    Campos opcionais devem vir como None quando não declarados no texto.
    Inferir o que não está escrito é considerado erro de extração.
    """
    cargo: str = Field(..., description="Cargo/título da vaga")
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
        return aliases.get(_normalizar_texto(valor), valor)

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
        return aliases.get(_normalizar_texto(valor), valor)


class RequestExtracao(BaseModel):
    """Corpo do POST /extrair."""
    texto: str = Field(..., min_length=1, description="Texto bruto do anúncio")
