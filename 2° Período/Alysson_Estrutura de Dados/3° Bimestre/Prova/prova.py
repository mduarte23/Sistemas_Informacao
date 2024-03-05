import json

with open("Prova/dados_prova.json", "r") as arquivo:
        dados_prova = json.load(arquivo)
print(dados_prova)

print ("LETRA A")
print("-"*20)
lista = []
for chave in dados_prova:
    nome = dados_prova[chave]
    lista.append(nome["nome"])

lista_organizada = sorted(lista)
print (lista_organizada)

print ("="*30)

print ("LETRA B")
print("-"*20)
l_idade = 0
velho = []
for chave in dados_prova:
    idade = dados_prova[chave]
    velho.append(idade["idade"])
maior_idade = max(velho)
idoso=[]
for chave in dados_prova:
    idade = dados_prova[chave]
    if idade["idade"] == maior_idade:
        idoso.append(idade["nome"])
print(f"Os mais velhos são: {idoso}")

print ("="*30)

print ("LETRA C")
print("-"*20)
l_idade = 0
novo = []
for chave in dados_prova:
    idade = dados_prova[chave]
    novo.append(idade["idade"])
menor_idade = min(novo)
jovem=[]
for chave in dados_prova:
    idade = dados_prova[chave]
    if idade["idade"] == menor_idade:
        jovem.append(idade["nome"])
print(f"Os mais novos são: {jovem}")

print ("="*30)

print ("LETRA D")
print("-"*20)
salario = 0
maior = []
for chave in dados_prova:
    salario = dados_prova[chave]
    maior.append(salario["salario"])
maior_salario = max(maior)

alto= []
for chave in dados_prova:
    salario = dados_prova[chave]
    if salario["salario"] == maior_salario:
        alto.append(salario["nome"])
print(f"Os maiores salários são: {alto}")


print ("LETRA E")
print("-"*20)
salario = 0
menor = []
for chave in dados_prova:
    salario = dados_prova[chave]
    menor.append(salario["salario"])
menor_salario = min(menor)

baixo= []
for chave in dados_prova:
    salario = dados_prova[chave]
    if salario["salario"] == menor_salario:
        baixo.append(salario["nome"])
print(f"Os menores salários são: {baixo}")



