from flask import Flask,request
from ibge import busca
#instanciar a aplicaçao 
app = Flask(__name__)


@app.route("/busca_nome")
def busca_nome():
    try: #tente
        #http://127.0.0.1:5000/busca_nome?nome=Marcelo
        var_nome = request.args.get("nome")
        response = busca(var_nome)
        
        #Percorrer o retorno e somar todas as ocorrencias do nome 

        return response


    except Exception as e: #se não #e nome do erro
        return f"Falha na rota /busca_nome: {e}"
   


#debug == True para nao ser necessario recarregar a app no navegador, por
app.run(debug=True)