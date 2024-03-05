# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 19:10:08 2023

@author: marce
"""

"""Faça um código python para gerar as tabelas:
    a) (A v B) <-> (¬A ^ ¬B)
    """
print ('-'*30)
print('(A v B) <-> (¬A ^ ¬B)')
    
possibilidades = [True, False]
contador = 0
verdadeiro= 0
falso = 0
for a in possibilidades:
    for b in possibilidades:
        contador +=1
        if (a or b) == (not a and not b):
            resultado = True
            verdadeiro+=1
        else:
            resultado = False
            falso+=1
        print (f'A = {a} \t B = {b} \t Resultado = {resultado}')
    
print(f'A tabela tem {contador} linhas!!!')
print(f'Tem {verdadeiro} possibilidades TRUE')
print(f'Tem {falso} possibilidades FALSE')
print ('-'*30)

""" b) (A <-> ¬(B ^ C)) v ¬((¬A v D) <-> (¬E ^ B))
    """
print ('-'*30)
print('(A <-> ¬(B ^ C)) v ¬((¬A v D) <-> (¬E ^ B))')

contador = 0
verdadeiro = 0
falso = 0

for a in possibilidades:
    for b in possibilidades:
        for c in possibilidades:
            for d in possibilidades:
                for e in possibilidades:
                    contador +=1
                    if (a == (not (b and c ))) or not((not a or d) == (not e and b)):
                        resultado = True
                        verdadeiro +=1
                    else:
                        resultado = False
                        falso +=1
                    print (f'A={a} \t B={b} \t C={c} \t D={d} \t E={e} \t Resultado={resultado}')
                    
print(f'A tabela tem {contador} linhas!!!')
print(f'Tem {verdadeiro} possibilidades TRUE')
print(f'Tem {falso} possibilidades FALSE')
print ('-'*30)    
                       
""" b) ((M ^ N) v (¬O <-> P)) ^ (¬(Q ^ M) v (N <-> P))
     """
print ('-'*30)
print('((M ^ N) v (¬O <-> P)) ^ (¬(Q ^ M) v (N <-> P))')

contador = 0
verdadeiro = 0
falso = 0
for m in possibilidades:
    for n in possibilidades:
        for o in possibilidades:
            for p in possibilidades:
                for q in possibilidades:
                    contador +=1
                    if ((m and n) or ( not o == p)) and (not(q and m ) or (n == p)):
                        resultado = True
                        verdadeiro+=1
                    else:
                        resultado = False
                        falso+=1
                    print (f'M = {m} \t N = {n} \t O = {o} \t P = {p} \t Q = {q} \t Resultado = {resultado}')
                    
print(f'A tabela tem {contador} linhas!!!')
print(f'Tem {verdadeiro} possibilidades TRUE')
print(f'Tem {falso} possibilidades FALSE')
print ('-'*30)    
            