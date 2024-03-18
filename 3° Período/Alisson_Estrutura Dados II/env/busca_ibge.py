from flask import Flask,request
from ibge import busca, calcula_ocorrencias, lista
#instanciar a aplicaçao 
app = Flask(__name__)


@app.route("/busca_nome")
def busca_nome():
    try: #tente
        #http://127.0.0.1:5000/busca_nome?nome=Marcelo
        var_nome = request.args.get("nome")
        response = busca(var_nome)
        soma = calcula_ocorrencias(response)

        objeto_retorno = {
            "nome_procurado": var_nome,
            "total_ocorrencia": soma
        }
        return objeto_retorno
        #Percorrer o retorno e somar todas as ocorrencias do nome 

       


    except Exception as e: #se não #e nome do erro
        return f"Falha na rota /busca_nome: {e}"
   
@app.route("/frequencia_min")
def minimo():
    try:
        nome = request.args.get("nome")
        response = busca(nome)
        data, qtd = lista(response)  # devolve o return da funcao em duas variaveis
        menor_numero = min(qtd) #pega o menor numero da lista 
        periodo = data[qtd.index(menor_numero)] #.index pega a posição do menor_numero na lista qtd


        retorno = {
            "Nome procurado": nome,
            "Periodo":  periodo,
            "Frequencia": menor_numero
        }
        return retorno

    except Exception as e:
        return f"Falha na rota /frequencia_min: {e}"
    
@app.route("/frequencia_max")
def maximo():
    try:
        nome = request.args.get("nome")
        response = busca(nome)
        data, qtd = lista(response)  # devolve o return da funcao em duas variaveis
        maior_numero = max(qtd) #pega o maior numero da lista 
        periodo = data[qtd.index(maior_numero)] #.index pega a posição do menor_numero na lista qtd
        retorno = {
            "Nome procurado": nome,
            "Periodo":  periodo,
            "Frequencia": maior_numero
        }
        return retorno

    except Exception as e:
        return f"Falha na rota /frequencia_max: {e}"

#debug == True para nao ser necessario recarregar a app no navegador, por
app.run(debug=True)