# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:32:08 2023

@author: marce
"""
print ('COMIDAS')
comidas = ['batata','lasanha','pudim','pastel','tapioca']

for X in comidas:
    print(X)
 
print ('-'*20)

print ('FRUTAS')
frutas = ['limão', 'banana','laranja','uva','melancia']

for y in frutas:
    print (y)
    
print ('-'*20)

print ('BEBIDAS')
bebidas = ['cerveja', 'guaraná','suco','vinho']

print ('COMBINAÇÃO DAS LISTAS')
for x in comidas:
    for y in frutas:
        for z in bebidas:
            
           print (x,y,z)