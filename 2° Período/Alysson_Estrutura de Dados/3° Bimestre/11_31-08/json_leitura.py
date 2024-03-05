import json 

#'r' - abrir para leitura
#'w' - abrir para escrita (sobrescreve)
#'a' - abrir para escrita (anexa no fim)
with open('11_31-08/base_dados/dados.json', 'r') as arquivo:
    registros = json.load(arquivo)

print (registros)
