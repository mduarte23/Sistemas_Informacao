from flask import Flask,request
from funcoes import lista

app = Flask(__name__)

@app.route("/distrito")
def distrito():
    try:
        retorno = lista()
        return retorno
    
    except Exception as e:
        return f"Falha na rota /distrito: {e}"
    
app.run(debug=True)