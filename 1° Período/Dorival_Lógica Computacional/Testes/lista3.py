# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 19:12:16 2023

@author: marce
"""

ListaNomes = ['Zé', 'Tião', 'Bob','Alice','Chaves']
print (len(ListaNomes))
print (f'Alista tem {len(ListaNomes)} itens')


print (f'Primeiro nome: {ListaNomes[0]}')
print (ListaNomes[0])
print (f'Quinto nome: {ListaNomes[4]}')
print (f'Quarto nome: {ListaNomes[3]}')

print (f'Lista Completa: {ListaNomes}')

print (f'Ultimo: {ListaNomes[-1]}')
print (f'Ultimo: {ListaNomes[len(ListaNomes)-1]}')

contador=0
for x in ListaNomes:
    contador+=1             
    print (f'Elemento {contador}: {x}')