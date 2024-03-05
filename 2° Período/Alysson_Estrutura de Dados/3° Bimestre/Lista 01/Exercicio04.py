"""4- Um dado é lançado 50 vezes, e o valor correspondente é armazenado em um vetor. Faça um programa que simule o lançamento do dado e determine o percentual de ocorrências de face 6 do dado dentre esses 50 lançamentos."""

import random
lancamento = 50
lista =[]
soma = 0
for x in range(lancamento):
    x = random.randint(1,6)
    lista.append(x)
    if x == 6:
        soma += 1
porcentagem = (soma / lancamento) * 100
print (f'O número 6 apareceu {soma} vezes, e a porcentagem foi de {porcentagem:.2f}%')



