import random
import time
lista = []
n_elementos = 20
for _ in range (n_elementos):
    lista.append(random.randint(0, 100000))

def busca_binaria(lista, elemento,inicio, fim):
    meio = (inicio + fim)//2
    if inicio < fim:
        if elemento == lista[meio]:
            return True
        elif elemento < lista[meio]:
            busca_binaria(lista, elemento, inicio, meio-1)
        elif elemento > lista[meio]:
            busca_binaria(lista, elemento, meio+1, fim)
    else:
        return False 
    
start = 