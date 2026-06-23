"""API HTTP da extração de vagas.

Sobe com:
    uvicorn main:app --reload

Documentação interativa: http://localhost:8000/docs
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from requests import RequestException

from schemas import RequestExtracao, Vaga
from ollama_client import extrair_vaga, ErroExtracao


app = FastAPI(
    title="API de Extração de Vagas",
    description="Extrai campos estruturados de anúncios de vagas usando LLM.",
    version="0.1.0",
)


@app.exception_handler(RequestValidationError)
async def tratar_erro_validacao_requisicao(
    request: Request, exc: RequestValidationError
):
    print(f"[validacao-requisicao] Endpoint: {request.method} {request.url.path}")
    print(f"[validacao-requisicao] Erros: {exc.errors()}")
    try:
        body = await request.body()
        print(f"[validacao-requisicao] Body bruto: {body[:1000]!r}")
    except Exception as e:
        print(f"[validacao-requisicao] Nao foi possivel ler o body: {e}")

    return JSONResponse(
        status_code=422,
        content=jsonable_encoder({"detail": exc.errors()}),
    )


@app.get("/")
def raiz():
    """Endpoint de saúde. Útil para verificar se o serviço está no ar."""
    return {"servico": "extracao-vagas", "status": "ok"}


@app.post("/extrair", response_model=Vaga)
def extrair(pedido: RequestExtracao) -> Vaga:
    """Recebe o texto de um anúncio e devolve a vaga estruturada.

    Retorna 422 se o modelo não conseguir estruturar a resposta.
    """
    try:
        print(f"[extrair] Request valido. Texto: {len(pedido.texto)} caracteres")
        return extrair_vaga(pedido.texto)
    except ErroExtracao as e:
        status_code = 503 if isinstance(e.__cause__, RequestException) else 422
        print(f"[extrair] ErroExtracao mapeado para HTTP {status_code}: {e}")
        raise HTTPException(status_code=status_code, detail=str(e)) from e
