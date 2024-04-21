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
    contador = 0
    for i in range (len(lista)):
        menor = i
        for j in range (i+1, len(lista)):
            contador += 1
            if lista[menor] > lista[j]:
                menor = j
            lista[i], lista[menor]= lista[menor], lista[i]
    #devolve a lista ordenada
    return lista, contador
    
#funçao para ordenar a lista por ordem alfabetica pelo bublle sort
def bublle_sort(lista):
    j = len(lista) - 1
    contador = 0
    while j > 0:
        #percorre a lista jogando o maior valor para o ultimo
        for i in range (0, j):
            contador += 1
            if lista[i] > lista[i+1]:
                #faz a troca das posições 
                lista[i] , lista[i+1] = lista[i+1], lista[i]
        #diminui o tamanho do proximo for
        j -= 1
    #devolve a lista ordenada
    return lista, contador

#funçao para ordenar a lista por ordem alfabetica pelo insertion sort
def insertion_sort(lista):
    contador = 0
    #percorre a lista pegando o i como referencia e j como chave de troca
    for i in range (1, len(lista)):
        chave = lista[i]
        j = i - 1
        #compara se o valores estão ordenados e faz a troca usando a variavel auxiliar
        while j >= 0 and lista[j] > chave:
            contador += 1
            lista [j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    #devolve a lista ordenada
    return lista, contador
   
def ordena(esquerda, direita, contador):   
    w_lista = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        contador += 1
        if esquerda[i] < direita[j]:
            w_lista.append(esquerda[i])
            i += 1
            
        else:
            w_lista.append(direita[j])
            j += 1
    
    w_lista.extend(esquerda[i:])
    w_lista.extend(direita[j:])

    return w_lista, contador

def merge_sort(lista):
    contador = 0
    #retorna a lista se ela for vazia ou se tiver só um item
    if len(lista) <= 1:
        return lista, contador
    #divide a lista ate ficar do tamanho 1 para usar a função ordena
    meio = len(lista)//2
    #monta a lista do inicio ate o meio
    esquerda = lista[:meio]
    #monta a lista do meio ate o fim
    direita = lista[meio:]
    #chamada recursiva passando as novas listas criadas
    esquerda, contador_esquerda = merge_sort(esquerda)
    direita, contador_direita = merge_sort(direita)
    #faz a soma das contagens de comparacoes
    contador = contador_esquerda + contador_direita
   
    resposta, contador = ordena(esquerda, direita, contador)
    return resposta, contador

def quick_sort(lista):
    ordenacao, contador = quickSortOrdena(lista, 0, len(lista)-1)
    return ordenacao, contador

def quickSortOrdena(lista, esq, dir):
    contador = 0
    if esq < dir:
        indice, lista, contador_esq = particao(lista, esq, dir, contador)
        #faz a soma das contagens
        contador += contador_esq
        #contador somando todas as chamadas recursivas
        contador += quickSortOrdena(lista, esq, indice-1)[1]
        contador += quickSortOrdena(lista, indice+1, dir)[1]
    return lista, contador

def particao (lista, esq, dir, contador):

    pivo = lista[esq]
    #particionamento
    i = esq
    j = dir
    while i <= j:
        #Encontrar elemento maior que o pivo
        while i <= dir and lista[i] <= pivo:
            i += 1
            contador += 1
        while j >= esq and  lista[j] > pivo:
            j -= 1
            contador += 1
        if i <= j:
            lista[i], lista[j] = lista[j], lista[i]

     #posiciona o pivo no local correto   
    lista[esq], lista[j] = lista[j], lista[esq]

    #retornar o indice do pivo e a contagem
    return j,lista, contador