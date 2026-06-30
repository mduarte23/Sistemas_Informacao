"""
Cliente para o servidor Ollama.

Isola toda a comunicação com o LLM. O resto da aplicação só chama
extrair_vaga() e recebe um objeto Vaga validado (ou um ErroExtracao).
"""

import os
import requests
from pydantic import ValidationError

from schemas import Vaga
from prompts import montar_prompt


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://23.22.22.5:11434")
MODELO = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

TIMEOUT_SEGUNDOS = 800


class ErroExtracao(Exception):
    """Erro genérico de extração. Será mapeado para HTTP 422/503 em main.py."""


def extrair_vaga(texto: str) -> Vaga:
    """
    Recebe o texto de um anúncio e devolve uma Vaga validada.

    Levanta ErroExtracao em caso de falha de comunicação, JSON inválido,
    ou validação Pydantic falhar.
    """

    prompt = montar_prompt(texto)

    payload = {
        "model": MODELO,
        "prompt": prompt,
        "stream": False,
        "format": "json",
    }

    print(f"[ollama] URL: {OLLAMA_URL}/api/generate")
    print(f"[ollama] Modelo: {MODELO}")
    print(f"[ollama] Texto recebido: {len(texto)} caracteres")
    print(f"[ollama] Prompt montado: {len(prompt)} caracteres")

    # =========================
    # 1ª tentativa
    # =========================
    try:
        resposta = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=TIMEOUT_SEGUNDOS,
        )
        print(f"[ollama] Status HTTP: {resposta.status_code}")
        resposta.raise_for_status()

    except requests.Timeout as e:
        raise ErroExtracao(f"Timeout ao chamar Ollama ({TIMEOUT_SEGUNDOS}s).") from e
    except requests.ConnectionError as e:
        raise ErroExtracao(f"Erro de conexão ao chamar Ollama: {OLLAMA_URL}") from e
    except requests.RequestException as e:
        raise ErroExtracao(f"Falha HTTP ao chamar Ollama: {e}") from e

    try:
        resposta_json = resposta.json()
    except ValueError as e:
        raise ErroExtracao(f"Ollama não retornou JSON válido: {e}") from e

    json_cru = resposta_json.get("response", "")

    print(f"[ollama] response tamanho: {len(json_cru)}")
    print(f"[ollama] preview: {json_cru[:500]!r}")

    # =========================
    # Validação Pydantic
    # =========================
    try:
        vaga = Vaga.model_validate_json(json_cru)
        print("[validacao] OK na primeira tentativa")
        return vaga

    except ValidationError as e:
        print("[validacao] Falhou na primeira tentativa, iniciando retry...")

        # =========================
        # Retry inteligente com erros
        # =========================

        erros_formatados = "\n".join(
            f"- {err.get('loc')} -> {err.get('msg')}"
            for err in e.errors()
        )

        prompt_retry = f"""
Você é um extrator de dados estruturados de vagas.

A resposta anterior falhou na validação do schema Vaga.

ERROS DETECTADOS:
{erros_formatados}

REGRAS IMPORTANTES:
- Corrija APENAS os campos com erro
- Mantenha todos os outros campos iguais se estiverem corretos
- Retorne APENAS JSON válido
- Não inclua texto extra
- Não use markdown

RESPOSTA ANTERIOR:
{json_cru[:2000]}

Agora corrija e retorne o JSON válido:
"""

    payload_retry = {
        **payload,
        "prompt": prompt_retry
    }

    # =========================
    # 2ª tentativa
    # =========================
    try:
        resposta_retry = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload_retry,
            timeout=TIMEOUT_SEGUNDOS,
        )
        print(f"[ollama] Status HTTP retry: {resposta_retry.status_code}")
        resposta_retry.raise_for_status()

    except requests.Timeout as e:
        raise ErroExtracao(f"Timeout no retry ({TIMEOUT_SEGUNDOS}s).") from e
    except requests.ConnectionError as e:
        raise ErroExtracao(f"Erro de conexão no retry: {OLLAMA_URL}") from e
    except requests.RequestException as e:
        raise ErroExtracao(f"Falha HTTP no retry: {e}") from e

    try:
        resposta_retry_json = resposta_retry.json()
    except ValueError as e:
        raise ErroExtracao(f"Retry não retornou JSON válido: {e}") from e

    json_retry = resposta_retry_json.get("response", "")

    print(f"[ollama] response retry tamanho: {len(json_retry)}")
    print(f"[ollama] preview retry: {json_retry[:500]!r}")

    # =========================
    # Validação final
    # =========================
    try:
        vaga = Vaga.model_validate_json(json_retry)
        print("[validacao] OK no retry")
        return vaga

    except ValidationError as e:
        print(f"[validacao] Falha final: {e.errors()}")
        raise ErroExtracao(
            "Modelo não conseguiu gerar JSON válido após retry."
        ) from e