# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:33:21 2023

@author: marce
"""

import numpy as np

matriz1 = np.arange(6, 11)
matriz2 = np.array([1, 2, 3, 4, 5])

print (f'Matriz 1: {matriz1}')
print (f'Matriz 2: {matriz2}')


matriz3 = matriz1 + matriz2
print (f'matriz 1 + matriz 2 : {matriz3}')

matriz4 = matriz1 - matriz2
print(f'matriz 1 - matriz 2 : {matriz4}')

matriz5 = matriz1 * matriz2
print (f'matriz 1 * matriz 2 : {matriz5}')

matriz6= matriz1 / matriz2
print (f'matriz1 / matriz2: {matriz6}') 

m8 = np.array([1,2,3,4,5])
print(f'Matriz m8: {m8}')

print (f'm8 + 2: {m8 + 2}')

print (f'm8 - 2: {m8 - 2}')

print (f'm8 * 2: {m8 * 2}')

print (f'm8 / 2: {m8 / 2}')

print (f'm8 ** 2: {m8 ** 2}')

matriz7= np.array([7,-3,4,2,7,3,8,9,1])
print (matriz7)

m7 = matriz7 > 5
print (m7)

