from flask import Flask, request
import requests
app = Flask(__name__)

@app.route("/usuario", methods=["GET"])
def index():
    try:
        user = request.arg.get("nome")
        idade = int(request.arg.get("idade"))
        return f"Ola {user} - {idade} anos"
    
    except:
        return "Falha!!!"
    
@app.route("/ibge", methods=["GET"])
def consulta_ibge():
    nome = request.args.get("nome")
    resposta = request.get(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}")
    return resposta.json()
    
app.run(debug=True)