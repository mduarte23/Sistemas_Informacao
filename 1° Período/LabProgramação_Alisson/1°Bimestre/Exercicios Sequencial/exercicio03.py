#exercicio 03
#Faça um programa que leia dois pontos num espaço bidimensional e calcule a distância entre esses pontos

import math

lat1= float(input('Digite a coordenada da latitude 1: '))
long1 = float(input('Digite a coordenada da longitude 1: '))
lat2= float(input('Digite a coordenada da latitude 2: '))
long2 = float(input('Digite a coordenada da latitude 2: '))

dist= math.sqrt((lat1-lat2)**2+(long1-long2)**2)
distancia = (((lat1-lat2)**2)+((long1-long2)**2))**0.5

print(f'A distância entre os pontos ({lat1},{long1}) e ({lat2},{long2}) é {distancia:.2f}')
print(f'A distancia entre os pontos ({lat1},{long2}) e ({lat2},{lat2}) é {dist:.2f} pela biblioteca math')