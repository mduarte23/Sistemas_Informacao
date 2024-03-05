# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 20:39:56 2023

@author: marce
"""

print('(((A^B)v(A^¬C))^(¬A<->D))<->(((¬AvE)^(¬E^F))v(¬D^¬F))^(¬BvG)')

possibilidades = [True, False]
contador = 0
verdadeiro = 0
falso = 0

for a in possibilidades:
    for b in possibilidades:
        for c in possibilidades:
            for d in possibilidades:
                for e in possibilidades:
                    for f in possibilidades:
                        for g in possibilidades:
                            contador+=1
                            if (((a and b)or(a and not c)) and (not a == d)) == (((not a or e)and (not e and f)) or (not d and not f))and (not b or g):
                                verdadeiro+=1
                                resultado = True
                            else:
                                falso+=1
                                resultado = False
                            print (f'A = {a} \t B = {b} \t C = {c} \t D = {d} \t E = {e} \t F = {f} \t G = {g} \t H = {resultado}')
                            
print(f'LETRA A: A tabela tem {contador} linhas')
print('-'*40)
print (f'LETRA B: A tabela tem {verdadeiro} linhas TRUE!')
print('-'*40)
print (f'LETRA C: A tabela tem {falso} linhas FALSE!')
                            
                            