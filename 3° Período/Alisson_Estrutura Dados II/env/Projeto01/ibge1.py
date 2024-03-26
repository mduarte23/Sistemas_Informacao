from flask import Flask,request
from funcoes import lista, nomes_cidades

app = Flask(__name__)

@app.route("/distrito")
def distrito():
    try:
        retorno = lista()
        teste = nomes_cidades(retorno)
        print (teste)
        return teste
    
    except Exception as e:
        return f"Falha na rota /distrito: {e}"
    


    
app.run(debug=True)