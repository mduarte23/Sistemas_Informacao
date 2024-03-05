# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 19:46:44 2023

@author: marce
"""

L_VAZIA = []
print (f'Questão 1: {L_VAZIA}')
print ('-'*30)

possibilidadeBoleanos = [True, False]
print(f'Questão 2: {possibilidadeBoleanos}')
print ('-'*30)

valores_Diversos = [1, -2, True, "Obabão", False, 1947, 5.3,-10]
print (f'Questão 3: {valores_Diversos}')
print ('-'*30)

print (f'Questão 4: Elemento da posição 1 é {valores_Diversos[1]} e elemento da posição 6 é {valores_Diversos[6]}')
print ('-'*30)

print (f'Questão 5: 2° elemento é {valores_Diversos[1]} e 4° elemento é {valores_Diversos[3]} ')
print ('-'*30)

tamanho = (len(valores_Diversos))
print (f'Questão 6: {tamanho}')
print ('-'*30)

print ('Questão 7:')
for x in valores_Diversos:    
    print (f' Elemento: {x}')
print (f'Quantidade de elementos: {len(valores_Diversos)}')
print ('-'*30)

BEBIDAS= ['Água', 'Suco', 'Cerveja', 'Vodka']
print (f'Questão 8: {BEBIDAS}')
print ('-'*30)

COMIDAS = ['Carne', 'Abacaxi', 'Arroz', 'Batata']
print (f'Questão 9: {COMIDAS}')
print ('-'*30)

print ('Questão 10:')
contador=0
for x in BEBIDAS:
    for y in COMIDAS:
        contador+=1
        print(f'Combinação {contador}: {x} e {y}')
print ('-'*30)
        
print('Questão 11:')
A= int(input('Digite o valor de A: '))
B= int(input('Digite o valor de B: '))
C= int(input('Digite o valor de C: '))
if ((A == 0) or (B == 0)) or ((C!=7) and (A!=7)):
    print ('OK')
else:
    print ("Negativo")
print ('-'*30)


print ('Questao 12:')   
altura = int(input('Valor de altura: '))
largura = int(input("Valor de largura: "))
if largura > altura  and largura == altura:
    print ('Verdadeiro')
else:
    print ('Falso')
print ('-'*30)
    




   