import json 

regis01 = {"nome": "Fulano", "idade": 10, "matriculado": True}
regis02 = {"nome": "Beltrana", "idade": 12, "matriculado": False}

dados = {"alunos":[regis01, regis02]}
print('Dicionário Python')
print (dados)

json_str = json.dumps(dados) #serializa o dicionario para json (transforma)
print('Formato Json')
print(json_str)

#salvar em arquivo
with open('11_31-08/base_dados/dados.json', "w") as json_file: #cria o arquivo json
    json.dump(dados, json_file, indent=4) #indent define identaçao no arquivo 