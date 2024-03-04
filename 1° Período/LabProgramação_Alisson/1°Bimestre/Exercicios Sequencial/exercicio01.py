#exercicio 01
#1- Faça um programa que leia o nome, a idade, a altura, o peso e a nacionalidade do usuário e escreva essas informações na forma de um parágrafo de apresentação

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
altura = float(input('Digite a altura em metros: '))
peso = float(input('Digite o peso: '))
nacionalidade = input('Digite a nacionalidade: ')

print(f'{nome} tem {idade} anos de idade, com altura de {altura} metros, peso de {peso} kg e sua nacionalidade é {nacionalidade}')