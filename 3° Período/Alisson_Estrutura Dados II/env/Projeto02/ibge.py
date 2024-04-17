from flask import Flask,request
import time
from funcoes import lista_cidades, nomes_cidades, selection_sort, bublle_sort, insertion_sort, merge_sort, quick_sort

app = Flask(__name__)

#Rota para buscar todas cidades do pais por ordem alfabetica
@app.route("/selection_sort")
def Selection_Sort():
    try:
        #lista = ['joao', 'maria', 'tiago', 'godofredo']
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao selection sort
        inicio = time.time()
        resposta, contador = selection_sort(cidades)
        fim = time.time()
        retorno = {
            "1-Algoritimo utilizado": "Selection Sort",
            "2-Tempo execução": fim-inicio ,
            "3-Numero de comparações ": contador, 
            "4-Lista de cidades": resposta 
        }
        print (f'Tempo execução {fim-inicio}')
        return retorno
    except Exception as e:
        return f"Falha na rota /distritos_ordenados: {e}"

@app.route("/bublle_sort")
def Bublle_Sort():
    try:
        #lista = ['joao', 'maria', 'tiago', 'godofredo','marcelo', "carol", "aline",'zumira', 'leonardo']
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao selection sort
        inicio = time.time()
        resposta = bublle_sort(cidades)
        fim = time.time()
        retorno = {
            "1-Algoritimo utilizado": "Selection Sort",
            "2-Tempo execução": fim-inicio ,
            "3-Lista de cidades": resposta 
        }
        print (fim-inicio)
        return retorno
    except Exception as e:
        return f"Falha na rota /distritos_ordenados: {e}"
    
@app.route("/insertion_sort")
def Insertion_Sort():
    try:
        #lista = ['joao', 'maria', 'tiago', 'godofredo','marcelo', "carol", "aline",'zumira', 'leonardo']
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao selection sort
        resposta = insertion_sort(cidades)
        return resposta
    except Exception as e:
        return f"Falha na rota /distritos_ordenados: {e}"
    
@app.route("/merge_sort")
def Merge_Sort():
    try:
        #lista = [9, 5, 7, 4, 6, 8]
        #lista = ['joao', 'maria', 'tiago', 'godofredo','marcelo', "carol", "aline",'zumira', 'leonardo']
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao selection sort
        resposta = merge_sort(cidades)
        return resposta
    except Exception as e:
        return f"Falha na rota /distritos_ordenados: {e}"
    
@app.route("/quick_sort")
def Quick_Sort():
    try:
        #lista = [9, 5, 7, 4, 6, 8]
        #lista = ['joao', 'maria', 'tiago', 'godofredo','marcelo', "carol", "aline",'zumira', 'leonardo']
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao selection sort
        resposta = quick_sort(cidades)
        return resposta
    except Exception as e:
        return f"Falha na rota /distritos_ordenados: {e}"
    
app.run(debug=True)