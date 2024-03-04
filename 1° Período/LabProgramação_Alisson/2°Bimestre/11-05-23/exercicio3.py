"""Programa para imprimir uma agenda diária, com horários de 15 em 15 minutos:

exemplo
00:00
00:15"""

for hora in range(0,24,1):
    for min in range(0,60,15):
        if min == 0:
            min= '00'
        print (f'{hora}:{min}')
