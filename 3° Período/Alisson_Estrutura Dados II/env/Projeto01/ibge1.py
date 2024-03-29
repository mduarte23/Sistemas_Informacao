from flask import Flask,request
from funcoes import lista_cidades, ordernar_cidades, busca_estado

app = Flask(__name__)

#ROta para buscar todas cidades do pais por ordem alfabetica
@app.route("/distritos_ordenados")
def distrito():
    try:
        json = lista_cidades()
        resposta = ordernar_cidades(json)
        return resposta
    except Exception as e:
        return f"Falha na rota /distritos_ordenados: {e}"

#rota para mostrar todas cidades do estado em ordem alfabetica
#nocessario passar    
@app.route("/cidades_do_estado")
def estados():
    try:
        estado = request.args.get("estado")
        json = busca_estado(estado)
        resposta = ordernar_cidades(json)
        return resposta
    except Exception as e:
        return f"Falha na rota /cidades_do_estado: {e}"
    
app.run(debug=True)