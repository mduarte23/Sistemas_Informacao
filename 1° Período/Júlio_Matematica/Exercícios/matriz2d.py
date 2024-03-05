# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 21:18:58 2023

@author: marce
"""

import numpy as np
M1 = np.array([[1,2],[3,4]])
print (f'Matriz 1: \n{M1}')

M2= np.array([[1,2],[3,4]])
print (f'\nMatriz 2: \n{M2}')

print(f'\nSoma das matrizes: \n {M1+M2}')
print(f'\nDiferença das matrizes: \n {M1-M2}')
#produto não faz operação correta
print(f'\nProduto das matrizes: \n {M1*M2}')
print(f'\nDivisão das matrizes: \n {M1/M2}')
#operação correta para multiplicação de matrizes
print('\nPara realmente fazer o produto entre as matrizes usamos: ')
print (M1.dot(M2))