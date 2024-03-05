"""
Faça um programa que gere números inteiros aleatórios entre 1 e 10 e calcule a soma desses números, até que seja gerado um número numérico que foi informado pelo usuário anterior.
----Dica 1: antes de mais nada, peça para o usuário digitar um número entre 1 e 10 e guarde o valor em num
----Dica2: use a função randint(inicio, fim) do módulo random para gerar um número aleatório entre 1 e 10
"""
import random

variavel= random.randint(1,10)
soma=0
numero= int(input('Digite um número de 1 à 10: '))
tentativas=0
print ('-'*50)
while numero < 1 or numero > 10:
    numero= int(input('Número incorreto, digite um número entre 1 e 10: '))

while numero != variavel:
    print(f'Número gerado aleatório: {variavel}')
    soma= soma + variavel
    variavel= random.randint(1,10)
    tentativas+=1
    
    
print ('-'*50)
print(f'A soma dos números gerados aleatoramente ate acertar o número {numero} foi de {soma}.')
if tentativas != 0:
    print(f'O numero de tentativas foi {tentativas}.')
else:
    print('Acertou de primeira tentativa.')
print ('-'*50)
