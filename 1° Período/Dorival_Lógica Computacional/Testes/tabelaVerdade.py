# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 20:48:54 2023

@author: marce
"""

vetorPossibilidade = [True, False]

print ("Testador de Fórmulas Tabajara 1.0")
print ("(A ^ B) v (¬A ^ ¬B)")
contador = 0
for a in vetorPossibilidade:
    for b in vetorPossibilidade:
        contador +=1
        if (a and b) or (not a and not b):
            resultadoF=True
        else:
            resultadoF=False
        print (f' A = {a} \t B = {b} \t Fórmula= {resultadoF}')
print (f'A tabela tem o total de {contador} linhas')
        

print ('-'*30)       
print ("Tabela 2 com contador de T e F")
print ("(C <-> D) ^ ¬(C v D)")
contador = 0
verdadeiro = 0
falso = 0
for c in vetorPossibilidade:
    for d in vetorPossibilidade:
        contador +=1
        if (c == d ) and not(c or d):
            resultado=True
            verdadeiro +=1
        else:
            resultado=False
            falso +=1
        print(f' C = {c} \t D = {d} \t Fórmula={resultado}')
        
print (f'A tabela tem o total de {contador} linhas')
print(f'A tabela tem {verdadeiro} linhas verdadeiras e {falso} linhas falsas')


print('-'*30)
print('Tabela 3')
print('(A v ¬(B <-> C)) ^ (¬A <-> C)')
contador = 0
verdadeiro = 0
falso = 0
for a in vetorPossibilidade: #A
    for b in vetorPossibilidade: #B
        for c in vetorPossibilidade: #C
            contador +=1
            if (a or not(b == c)) and (not a == c):
                resultado= True
                verdadeiro +=1
            else:
                resultado= False
                falso +=1
            print(f' A = {a} \t B = {b} \t C = {c} \t Resultado = {resultado}')

print (f'A tabela tem {contador} linhas, sendo {verdadeiro} True e {falso} False.')
       
        
    
        