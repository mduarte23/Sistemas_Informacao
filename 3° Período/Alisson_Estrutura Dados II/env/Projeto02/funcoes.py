import requests
import unicodedata

#função para remover os acentos
def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')

#função para deixar toda a lista minuscula
def minusculo(lista):
    for i in range(len(lista)):
        lista[i]= lista[i].lower()
    return lista

#função para gerar o json de todas cidades completo
def lista_cidades():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
    resposta = requests.get(url)
    return resposta.json()


#função para criar a lista de cidades e tirar acentuação
def nomes_cidades(lista):
    cidades = []
    for cidade in lista:
        #nome recebe o nome da cidade, se não tiver nada rebebe None
        nome = cidade.get("nome", None)
        #verifica so a variavel nome nao esta vazia, se nao estiver adiciona o nome no array teste
        if nome != None:
            cidades.append(nome)
    #cria a lista sem acentuação   
    cidades_sem_acentos= [remover_acentos(verificar) for verificar in cidades]
    #chama a função para deixa as letras minusculas
    cidades_sem_acentos= minusculo(cidades_sem_acentos)    

    return cidades_sem_acentos

#função para ordenar a lista por ordem alfabetica pelo selection sort
def selection_sort(lista):
    for i in range (len(lista)):
        menor = i
        for j in range (i+1, len(lista)):
            if lista[menor] > lista[j]:
                menor = j
            lista[i], lista[menor]= lista[menor], lista[i]
    return lista
    
#funçao para ordenar a lista por ordem alfabetica pelo bublle sort
def bublle_sort(lista):
    j = len(lista) - 1
    while j > 0:
        for i in range (0, j):
            if lista[i] > lista[i+1]:
                lista[i] , lista[i+1] = lista[i+1], lista[i]
            j += 1
    return lista
   


