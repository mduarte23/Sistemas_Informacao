#2. Faça um programa que exiba o perímetro de uma circunferência a partir do seu raio 
#exercicio 02

import math #importando biblioteca matematica
raio = float(input('Digite o valor do raio em metros: '))
perimetro = 2*3.14*raio
comprimento = 2*math.pi* raio

print(f'O perímetro da circunferência é {perimetro:.2f} metros')
print (f'O valor do perímetro com o PI valor exato é {comprimento:.2f}')