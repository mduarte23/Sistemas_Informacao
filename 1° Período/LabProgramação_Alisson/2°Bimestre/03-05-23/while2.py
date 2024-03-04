"""Programa que imprime a quantidade de números pares de 100 a 200, incluindo-os"""
numero = 100
par = 0

while numero <= 200:
    if numero % 2 == 0:  # % resto da divisão
        par += 1
    numero += 1

print (f'Existem {par} números pares entre 100 e 200')