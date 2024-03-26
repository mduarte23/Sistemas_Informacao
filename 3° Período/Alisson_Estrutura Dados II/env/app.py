from flask import Flask,request

#instanciar a aplicaçao 
app = Flask(__name__)

@app.route("/")
def index():
    return "aplicacao online"

@app.route("/calcula", methods=["GET"])
def calcula():
    #http://127.0.0.1:5000/calcula?qtd=50&preco=5
    print (str(request))
    print(request.args) #args leva as caracteristicas do objeto
    print (request.args.get("qtd")) #get pega o valor da chave passada
    
    
    quantidade = request.args.get("qtd")
    preco = request.args.get("preco")
    if quantidade is not None and preco is not None:
        return f"R$ {int(quantidade)*int(preco)}"
    
    return "Um dos parametros não foi passado"

@app.route("/paridade", methods=["GET"])
def paridade():
    numero = request.args.get("valor")
    if int(numero) %2 == 0:
        return f"{numero} é par"
    else:
        return f"{numero} é impar"
    
    #return verifica_par(param_valor)

#def verifica_par(numero):
    #return numero % 2 == 0 #retorna True ou False


#rodar a app
#debug == True para nao ser necessario recarregar a app no navegador, por
    
"""Crie uma rota somar_ate que tera um parametro valor recebido na requisição.
A rota devera somar todos os numeros ate o valor
exemplo: s o valor == 10
retorno deve se a soma de 1+2+3+...+10"""

@app.route ("/somar_ate", methods=["GET"])
def somar_ate():
    #http://127.0.0.1:5000/somar_ate?numero=10
    numero = request.args.get("valor")
    soma = 0
    resultado = 0
    if int(numero) > 0:
        while soma <= int(numero):
            resultado = resultado + soma
            soma += 1
            #print (resultado)
        return f"A soma dos números ate o número {numero} é {resultado}"
    else:
        return "O número tem que ser positivo"
    
    

app.run(debug=True)
