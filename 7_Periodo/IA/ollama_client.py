"""Cliente para o servidor Ollama.

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
# Preciso aumentar timeaut de 120 para 
TIMEOUT_SEGUNDOS = 300


class ErroExtracao(Exception):
    """Erro genérico de extração. Será mapeado para HTTP 422/503 em main.py."""


def extrair_vaga(texto: str) -> Vaga:
    """Recebe o texto de um anúncio e devolve uma Vaga validada.

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

    try:
        resposta = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload,
            timeout=TIMEOUT_SEGUNDOS,
        )
        print(f"[ollama] Status HTTP: {resposta.status_code}")
        resposta.raise_for_status()
    except requests.Timeout as e:
        print(f"[ollama] Timeout apos {TIMEOUT_SEGUNDOS} segundos: {e}")
        raise ErroExtracao(
            f"Timeout ao chamar Ollama apos {TIMEOUT_SEGUNDOS} segundos."
        ) from e
    except requests.ConnectionError as e:
        print(f"[ollama] Erro de conexao: {e}")
        raise ErroExtracao(f"Erro de conexao ao chamar Ollama em {OLLAMA_URL}: {e}") from e
    except requests.RequestException as e:
        print(f"[ollama] Falha HTTP/comunicacao: {e}")
        raise ErroExtracao(f"Falha ao chamar Ollama: {e}") from e

    try:
        resposta_json = resposta.json()
    except ValueError as e:
        print(f"[ollama] Resposta nao era JSON: {resposta.text[:1000]!r}")
        raise ErroExtracao(f"Ollama retornou resposta que nao e JSON: {e}") from e

    print(f"[ollama] Chaves da resposta: {list(resposta_json.keys())}")
    json_cru = resposta_json.get("response", "")
    print(f"[ollama] Campo response: {len(json_cru)} caracteres")
    print(f"[ollama] Preview response: {json_cru[:1000]!r}")

    try:
        vaga = Vaga.model_validate_json(json_cru)
        print("[validacao-vaga] Schema Vaga validado com sucesso")
        return vaga
    except ValidationError as e:
        print(f"[validacao-vaga] Erros Pydantic: {e.errors()}")
        print("[validacao-vaga] Tentando novamente com prompt mais estrito")

    prompt_retry = (
        f"{prompt}\n\n"
        "A resposta anterior nao era um JSON valido para o schema Vaga.\n"
        "Retorne APENAS um objeto JSON, sem markdown e sem texto extra.\n"
        "Inclua obrigatoriamente todas as chaves: cargo, empresa, localidade, "
        "modalidade, nivel, salario, requisitos, beneficios.\n"
        "Use null para valores ausentes, listas vazias para requisitos/beneficios "
        "ausentes e modalidade apenas como remoto, hibrido ou presencial.\n"
        f"Resposta anterior: {json_cru[:2000]!r}\n"
    )
    payload_retry = {**payload, "prompt": prompt_retry}

    try:
        resposta_retry = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload_retry,
            timeout=TIMEOUT_SEGUNDOS,
        )
        print(f"[ollama] Status HTTP retry: {resposta_retry.status_code}")
        resposta_retry.raise_for_status()
    except requests.Timeout as retry_timeout:
        print(f"[ollama] Timeout no retry apos {TIMEOUT_SEGUNDOS} segundos: {retry_timeout}")
        raise ErroExtracao(
            f"Timeout ao chamar Ollama apos {TIMEOUT_SEGUNDOS} segundos."
        ) from retry_timeout
    except requests.ConnectionError as retry_connection_error:
        print(f"[ollama] Erro de conexao no retry: {retry_connection_error}")
        raise ErroExtracao(
            f"Erro de conexao ao chamar Ollama em {OLLAMA_URL}: {retry_connection_error}"
        ) from retry_connection_error
    except requests.RequestException as retry_request_error:
        print(f"[ollama] Falha HTTP/comunicacao no retry: {retry_request_error}")
        raise ErroExtracao(f"Falha ao chamar Ollama: {retry_request_error}") from retry_request_error

    try:
        resposta_retry_json = resposta_retry.json()
    except ValueError as retry_json_error:
        print(f"[ollama] Resposta retry nao era JSON: {resposta_retry.text[:1000]!r}")
        raise ErroExtracao(
            f"Ollama retornou resposta que nao e JSON: {retry_json_error}"
        ) from retry_json_error

    json_retry = resposta_retry_json.get("response", "")
    print(f"[ollama] Campo response retry: {len(json_retry)} caracteres")
    print(f"[ollama] Preview response retry: {json_retry[:1000]!r}")

    try:
        vaga = Vaga.model_validate_json(json_retry)
        print("[validacao-vaga] Schema Vaga validado com sucesso no retry")
        return vaga
    except ValidationError as retry_validation_error:
        print(f"[validacao-vaga] Erros Pydantic no retry: {retry_validation_error.errors()}")
        raise ErroExtracao(
            f"Modelo retornou JSON que nao bate com o schema Vaga: {retry_validation_error}"
        ) from retry_validation_error
