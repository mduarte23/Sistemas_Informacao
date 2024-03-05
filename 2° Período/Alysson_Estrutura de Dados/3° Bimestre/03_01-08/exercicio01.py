"""Faça um programa que leia o nome de 5 pessoas e armazene em uma lista de nomes
No final imprima na tela uma mensagem de boas vindas para cada nome armazenado.
Ex.: 
nomes = ['Turing', 'Ada', 'Linus', 'Dijkstra']
Seja bem vindo(a) Turing
"""
quantidade = 5
nomes = []
for i in range(quantidade):
    nomes.append(input(f'Digite o {i +1}° nome: '))
for nome in nomes:
    print (f'Olá, seja bem vindo(a) {nome.upper()}!')
