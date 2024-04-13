from flask import Flask,request
from funcoes import lista_cidades, nomes_cidades, selection_sort, bublle_sort

app = Flask(__name__)

#Rota para buscar todas cidades do pais por ordem alfabetica
@app.route("/selection_sort")
def Selection_Sort():
    try:
        #lista = ['joao', 'maria', 'tiago', 'godofredo']
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao selection sort
        resposta = selection_sort(cidades)
        return resposta
    except Exception as e:
        return f"Falha na rota /distritos_ordenados: {e}"

@app.route("/bublle_sort")
def Bublle_Sort():
    try:
        #lista = ['joao', 'maria', 'tiago', 'godofredo']
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao selection sort
        resposta = bublle_sort(cidades)
        return resposta
    except Exception as e:
        return f"Falha na rota /distritos_ordenados: {e}"
    
app.run(debug=True)