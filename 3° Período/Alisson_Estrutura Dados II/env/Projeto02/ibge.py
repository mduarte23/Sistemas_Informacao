from flask import Flask,request
import time
from funcoes import lista_cidades, nomes_cidades, selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort

app = Flask(__name__)

@app.route("/selection_sort")
def Selection_Sort():
    try:
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
        return f"Falha na rota /selection_sort: {e}"

@app.route("/bubble_sort")
def Bubble_Sort():
    try:
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao bulle sort
        inicio = time.time()
        resposta, contador = bubble_sort(cidades)
        fim = time.time()
        retorno = {
            "1-Algoritimo utilizado": "Bubble Sort",
            "2-Tempo execução": fim-inicio ,
            "3-Numero de comparações ": contador,
            "4-Lista de cidades": resposta 
        }
        
        return retorno
    except Exception as e:
        return f"Falha na rota /bubble_sort: {e}"
    
@app.route("/insertion_sort")
def Insertion_Sort():
    try:
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao insertion sort
        inicio = time.time()
        resposta, contador = insertion_sort(cidades)
        fim = time.time()
        retorno = {
            "1-Algoritimo utilizado": "Insertion Sort",
            "2-Tempo execução": fim-inicio ,
            "3-Numero de comparações ": contador,
            "4-Lista de cidades": resposta 
        }
        return retorno
    except Exception as e:
        return f"Falha na rota /insertion_sort: {e}"
    
@app.route("/merge_sort")
def Merge_Sort():
    try:
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao merge sort
        inicio = time.time()
        resposta, contador = merge_sort(cidades)
        fim = time.time()
        retorno = {
            "1-Algoritimo utilizado": "Merge Sort",
            "2-Tempo execução": fim-inicio ,
            "3-Numero de comparações ": contador,
            "4-Lista de cidades": resposta 
        }
        return retorno
    except Exception as e:
        return f"Falha na rota /merge_sort: {e}"
    
@app.route("/quick_sort")
def Quick_Sort():
    try:
        #chama uma funçao passando outra funcao como parametro
        cidades = nomes_cidades(lista_cidades())
        #chama a função de ordençao quik sort
        inicio = time.time()
        resposta, contador= quick_sort(cidades)
        fim = time.time()
        retorno = {
            "1-Algoritimo utilizado": "Quick Sort",
            "2-Tempo execução": fim-inicio ,
            "3-Numero de comparações ": contador,
            "4-Lista de cidades": resposta 
        }
        return retorno
    except Exception as e:
        return f"Falha na rota /quick_sort: {e}"
    
app.run(debug=True)