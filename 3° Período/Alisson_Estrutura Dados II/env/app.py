from flask import Flask,request

#instanciar a aplicaçao 
app = Flask(__name__)

@app.route("/")
def index():
    return "aplicacao online"

@app.route("/calcula", methods=["GET"])
def calcula():
    quantidade = int(request.args.get("qtd"))
    preco = int(request.args.get("preco"))
    return f"R$ {quantidade*preco}"


#rodar a app
#debug == True para nao ser necessario recarregar a app no navegador, por

app.run(debug=True)
