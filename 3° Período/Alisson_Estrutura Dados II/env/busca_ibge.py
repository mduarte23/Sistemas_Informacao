from flask import Flask,request

#instanciar a aplicaçao 
app = Flask(__name__)


@app.route("/busca_nome")
def busca():
    try: #tente
        var_nome = request.args.get("nome")
        return var_nome

    except Exception as e: #se não #e nome do erro
        return f"Falha na rota /busca_nome: {e}"

#debug == True para nao ser necessario recarregar a app no navegador, por
app.run(debug=True)