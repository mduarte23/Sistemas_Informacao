# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:23:29 2023

@author: marce

contrditoria = todos falsos]
tautologica = todos verdadeiros
satisfatoria = verdadeiro e falso
"""

vetorPossibilidade = [True, False]
contador = 0
verdadeiro = 0
falso = 0
print ("Testador de Fórmulas Tabajara 1.0")
variaveis= int(input('Quantas variáveis tem a sua fórmula? 2 ou 3?: '))
while variaveis != 2 and variaveis != 3:
    variaveis= int(input('Opção inválida, digite novamente.'))

if variaveis == '2':
    formula = input('Digite a formula: ')

    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            contador +=1
            if eval(formula):
                resultadoF=True
                verdadeiro+=1
            else:
                resultadoF=False
                falso+=1
            print (f' A = {a} \t B = {b} \t Fórmula= {resultadoF}')
    
else:
    formula = input('Digite a formula: ')

    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            for c in vetorPossibilidade:
                contador +=1
                if eval(formula):
                    resultadoF=True
                    verdadeiro+=1
                else:
                    resultadoF=False
                    falso+=1
                print (f' A = {a} \t B = {b} \t C = {c} \t Fórmula= {resultadoF}')
            
if verdadeiro == contador:
    print('A fórmula é TAUTOLÓGICA.')
elif falso == contador:
    print('A fórmula é CONTRADITÓRIA.')
else:
    print('A fórmula é SATISFATÓRIA.')
print(f'A tabela tem {contador} linhas!!!')
print(f'Tem {verdadeiro} possibilidades TRUE')
print(f'Tem {falso} possibilidades FALSE')
print ('-'*30) 
            