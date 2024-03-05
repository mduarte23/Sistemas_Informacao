"""01 - Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faça um programa que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo
"""

lista=[12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

print('A')
maior= max(lista)
print (f'O maior elemento é {maior}')
print ('-'*30)

print ('B')
menor = min(lista)
print (f'O menor elemento é {menor}')
print ('-'*30)

print ('C')
pares = "Os números pares são: "
for x in lista:
    if x % 2 == 0:
        x = str(x)
        pares = pares + x + ", "
print (pares[:-2])

print ('-'*30)

print ('D')
tmp = 0
for x in lista:
    if x == 12:
        tmp += 1
print (f"O numero {lista[0]} aparece {tmp} vezes.")
print ('-'*30)

print ('E')
soma = 0
for x in lista:
    soma = soma + x
media = soma / len(lista)
print (f'A média da lista é {media:.2f}')
print ('-'*30)

print ('F')
negativos = 0
for x in lista:
    if x < 0:
        negativos = negativos + x
print (f'A soma dos elementos negativos é {negativos}')