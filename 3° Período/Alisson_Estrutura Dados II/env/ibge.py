import requests #faz a requisição de algum endereço on-line



def busca(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    resposta = requests.get(url)
    return resposta.json() #retorna lista em JSON

def retorn_lista(lista):
    conteudo = lista[0] #cria a lista de nomes
    return conteudo.get("res", [])  #tenta acessar a chave res, se não achar devolve uma lista vazia

def calcula_ocorrencias(json):
    resposta = retorn_lista(json)
    soma = []
    for elemento in resposta:
        frequencia = elemento.get("frequencia", 0) #pega a chave frequencia, se não tiver retorna 0 para tratar erros
        soma.append(frequencia)

    return sum(soma)
        
def lista(json):
    resposta = retorn_lista(json)
    periodo = []
    frequencia = []
    for elemento in resposta:
        data = elemento.get("periodo", 0)
        qtd = elemento.get("frequencia", 0)
        periodo.append(data) #cria uma lista dos periodos
        frequencia.append(qtd) #cria uma lista das frequencias
    return periodo, frequencia #devolve duas listas em 2 variaveis diferentes

#selection sort
def lista_crescente(json):
    periodo, frequencia = lista(json)
    print (periodo)
    print (frequencia)
    
    for i in range (len(frequencia)):
        menor = i #pega o indice
        for j in range (i+1, len(frequencia)):
            if frequencia[menor] > frequencia[j]:
                menor = j #pega o indice para trocar
                periodo[i], periodo[menor] = periodo[menor], periodo[i] #faz a troca de posiçoes 
                frequencia[i], frequencia[menor] = frequencia[menor], frequencia[i] #faz a troca de posiçoes   
    retorno = {}
    for i in range(len(frequencia)): #cria o dicionario da lista ordenada
        retorno[i] = str(frequencia[i]) +" : " + periodo[i]
    return retorno
    
def bublle_sort(lista_periodo, lista_qtd):
    j = len(lista_qtd) - 1
    while j > 0:
        for i in range (0,j):
            if lista_qtd[i] > lista_qtd[i+1]:
                lista_qtd[i], lista_qtd[i+1] = lista_qtd[i+1], lista_qtd[i]
                lista_periodo[i], lista_periodo[i+1] = lista_periodo[i+1], lista_periodo[i]
                print (lista_qtd)
                #print (lista_periodo)
            j += 1
        print (lista_qtd)
    retorno = {}
    for i in range(len(lista_qtd)): #cria o dicionario da lista ordenada
        #print (lista_periodo[i])
        #print (lista_qtd)
        retorno[i] = str(lista_periodo[i]) +" : " + lista_qtd[i]
        print (retorno)
    return retorno   
