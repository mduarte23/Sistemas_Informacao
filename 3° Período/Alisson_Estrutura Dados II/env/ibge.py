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

def lista_crescente(json):
    periodo, frequencia = lista(json)
    print (periodo)
    print (frequencia)
    
    for i in range (len(frequencia)):
        menor = i
        for j in range (i+1, len(frequencia)):
            if frequencia[menor] > frequencia[j]:
                menor = j
                periodo[i], periodo[menor] = periodo[menor], periodo[i]
                frequencia[i], frequencia[menor] = frequencia[menor], frequencia[i]
                

    #print (periodo)
    #print (frequencia)
    
    retorno = []
    for i in range(len(frequencia)):
        retorno.append(frequencia[i])

    print (f"O {retorno}")
    return retorno
    

#teste = busca("Jose")
#print (teste)