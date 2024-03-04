"""
E se o enunciado fosse "Faça um programa que soma x números gerados aleatoriamente no intervvalo de 1 a 10, onde x é informado pelo usuário"?
"""
import random

variavel= random.randint(1,10)
soma=0

x = int(input('Digite a quantidade de tenttivas que deseja realizar: '))

print ('-'*50)

##PARA UMA REPETIÇAO CONTAVEL

for tentativas in range(0,x): #ou for tentativas in range (x): ###range sempre começa do 0
    print(f'Número gerado aleatório: {variavel}')
    soma= soma + variavel
    variavel= random.randint(1,10)
   
    
    
print ('-'*50)
print(f'A soma dos números gerados aleatoramente foi de {soma}.')

print ('-'*50)
