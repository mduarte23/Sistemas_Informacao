# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:04:40 2023

@author: marce
"""

NOME = input('Digite o seu nome: ')
NOTA1 = float(input('Primeira nota: '))
NOTA2 = float(input('Segunda nota: '))
NOTA3 = float(input('Terceira nota: '))
NOTA4 = float(input('Quarta nota: '))

MEDIA = (NOTA1 + NOTA2 + NOTA3 + NOTA4) / 4

FALTA = 70 - MEDIA

print(f"Média final:{MEDIA}")


if (MEDIA >= 70):
    print (f'Parabêns {NOME}, você foi aprovado')
else:
    print(f'{NOME}, você esta reprovado. Faltam {FALTA} pontos para a média minima.')
    