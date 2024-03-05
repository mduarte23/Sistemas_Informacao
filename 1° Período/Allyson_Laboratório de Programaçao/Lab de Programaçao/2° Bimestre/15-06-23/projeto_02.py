"""Codifique um algoritimo que exiba um histograma da variação da temperatura durante a semana. Por exemplo, se as temperaturas forem: 19, 21, 25, 22, 20, 17, e 15°C, de domingo a sábado, respectivamente, o algoritmo deverá exibir:
D: *******************
S: *********************
T: *************************
Q: **********************
Q: ********************
S: *****************
S: *******************
Suponha que as temperaturas sejam todas positivas e que nenhuma seja maior que 80°C
"""
import os

domingo= int(input('Digite a temperatura em °C registrada no Domingo: '))
while domingo <= 0 or domingo > 80:
    domingo= int(input('Temperatura fora da margem, tente uma temperatura entre 1°C e 80°C: '))

segunda= int(input('Digite a temperatura em °C registrada no Segunda-Feira: '))
while segunda <= 0 or segunda > 80:
    segunda= int(input('Temperatura fora da margem, tente uma temperatura entre 1°C e 80°C: '))

terca= int(input('Digite a temperatura em °C registrada no Terça-Feira: '))
while terca <= 0 or terca > 80:
    terca= int(input('Temperatura fora da margem, tente uma temperatura entre 1°C e 80°C: '))

quarta= int(input('Digite a temperatura em °C registrada no Quarta-Feira: '))
while quarta <= 0 or quarta > 80:
    quarta= int(input('Temperatura fora da margem, tente uma temperatura entre 1°C e 80°C: '))

quinta= int(input('Digite a temperatura em °C registrada no Quinta-Feira: '))
while quinta <= 0 or quinta > 80:
    quinta= int(input('Temperatura fora da margem, tente uma temperatura entre 1°C e 80°C: '))

sexta= int(input('Digite a temperatura em °C registrada no Sexta-Feira: '))
while sexta <= 0 or sexta > 80:
    sexta= int(input('Temperatura fora da margem, tente uma temperatura entre 1°C e 80°C: '))

sabado= int(input('Digite a temperatura em °C registrada no Sábado: '))
while sabado <= 0 or sabado > 80:
    sabado= int(input('Temperatura fora da margem, tente uma temperatura entre 1°C e 80°C: '))

os.system('cls')
print('Histograma da variação de temperatura na semana:')
print(f'D: {"*" * domingo}')
print(f'S: {"*" * segunda}')
print(f'T: {"*" * terca}')
print(f'Q: {"*" * quarta}')
print(f'Q: {"*" * quinta}')
print(f'S: {"*" * sexta}')
print(f'S: {"*" * sabado}')
