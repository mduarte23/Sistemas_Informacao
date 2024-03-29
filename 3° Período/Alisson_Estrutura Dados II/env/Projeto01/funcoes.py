import requests
import unicodedata

#função para remover os acentos
def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')

#função para gerar o json de todas cidades
def lista_cidades():
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/distritos"
    resposta = requests.get(url)
    return resposta.json()

#funçao para gerar o json de todas cidades do estado
def busca_estado(estado):
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/distritos"
    resposta = requests.get(url)
    #retorna a lista em json
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
        
    return cidades_sem_acentos

#função para ordenar a lista por ordem alfabetica
def ordernar_cidades(json):
    #chama a funcao nomes_cidade
    lista = nomes_cidades(json)
    #organiza por ordem alfabetica
    lista.sort
    ordenada = sorted(lista)

    return ordenada


