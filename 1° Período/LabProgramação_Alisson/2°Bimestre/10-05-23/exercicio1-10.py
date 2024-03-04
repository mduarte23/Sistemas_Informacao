"""
E se o enunciado fosse "Faça um programa que soma x números gerados aleatoriamente no intervvalo de 1 a 10, onde x é informado pelo usuário"?
"""
import random

variavel= random.randint(1,10)
soma=0
tentativas=0
x = int(input('Digite a quantidade de tenttivas que deseja realizar: '))

print ('-'*50)



while tentativas < x:
    print(f'Número gerado aleatório: {variavel}')
    soma= soma + variavel
    variavel= random.randint(1,10)
    tentativas+=1
    
    
print ('-'*50)
print(f'A soma dos números gerados aleatoramente foi de {soma}.')

print ('-'*50)
