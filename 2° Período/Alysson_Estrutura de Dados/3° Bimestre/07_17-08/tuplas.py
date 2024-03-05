"""
Utilizando lista ou tuplas faça um programa que faça 5 perguntas para uma pessoa sobre o crime. As perguntas são:
a- "Telefonou para a vítima?"
b- "Esteve no local do crime?"
c- "Mora perto da vítima?"
d- "Devia para a vítima?"
e- "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificaçao sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questão ela deve ser classificada como "Suspeita", entre 3 e 4 "Cumplice", e 5 como "Assassino". caso contrário, ele será classificado como "Inocente". 
"""

perguntas = ("Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?")
contador = 0

for i in perguntas:
    resposta = input(i + "S ou N: ").upper()
    if resposta == "S":
        contador +=1
if contador >= 5:
    print ("Assassino")
elif contador >= 3:
    print ("Cumplice")
elif contador >= 2:
    print ("Suspeita")
else:
    print("Inocente")