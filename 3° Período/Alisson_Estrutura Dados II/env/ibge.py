import requests #faz a requisição de algum endereço on-line



def busca(nome):
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"
    resposta = requests.get(url)
    return resposta.json()

def calcula_ocorrencias(json):
    conteudo = json[0]
    resposta = conteudo.get("res", []) #tenta acessar a chave res, se não achar devolve uma lista vazia
    soma = []
    for elemento in resposta:
        frequencia = elemento.get("frequencia", 0) #pega a chave frequencia, se não tiver retorna 0 para tratar erros
        soma.append(frequencia)

    return sum(soma)
        
def lista(json):
    conteudo = json[0]
    resposta = conteudo.get("res", [])
    periodo = []
    frequencia = []
    for elemento in resposta:
        data = elemento.get("periodo", 0)
        qtd = elemento.get("frequencia", 0)
        periodo.append(data)
        frequencia.append(qtd)
    return periodo, frequencia


#teste = busca("Jose")
#print (teste)