"""
Escreva um programa que remova todos os elementos da primeira lista que tambem estao presentes na segunda lista
"""

lista1=[4,5,2,3,1,2,5]
lista2 = [3,1,5,8,9]

lista1= set(lista1) #transforma a lista em conjunto
lista2 = set(lista2)

resultado = lista1.difference(lista2)
print(resultado)

