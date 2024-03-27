import requests

def lista():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
    resposta = requests.get(url)
    return resposta.json()

def nomes_cidades(lista):
    teste = lista()
    for i in range (0,len(teste)):
        conteudo = lista[i]["id"]
        print (conteudo)
        teste.append = conteudo.get("nome", [])
    print (teste)
    return teste