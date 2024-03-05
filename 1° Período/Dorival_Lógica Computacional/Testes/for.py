# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 20:44:09 2023

@author: marce

"""


print ('Exercício 1')
for A in [10,19,24,23,50.1]:
    print(f'Agora o A vale: {A}')
    print ('-' * 20)
print ('='*20)

print ('Exercicio 2')
B= [10,19,24,23,50.1]
for X in B:
    print (f'Agora o B vale: {X}')
    print ('-' * 20)
print ('='*20)

C = [True, False]
for Z in C:
    print (f'Agora o C vale: {Z}')
    print ('-' * 20)
print ('='*20)

#Valor inicial e ultimo valor
for D in range(0,6):
    print (f'Valor de D: {D}')
    print ('-' * 20)
print ('='*20)

for E in range (0,20,2):
    print (f'Valor de E: {E}')
    print ('-' * 20)
print ('='*20)

F = 0
while F < 10:
    F=float(input('Digite um Valor: '))

senha= '123456'
m =''
while m != senha:
    m=input ('Digite a senha: ') 

nota = float(input('Digite uma nota de 0 - 100: '))
while nota <0 or nota >100:
    nota = float(input('Nota inválida, tente novamente: '))
print (f'A nota digitada foi {nota}')


"""
numero = 50
tentativa = int(input('Digite um número: '))

while numero < 50:
    tentativa = int(input('Maior, tente novamente:  ')
"""
                    
