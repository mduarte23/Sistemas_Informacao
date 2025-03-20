#Adicione elementos de forma aleatoria em uma matriz NxM e retorne a quantidade de numero pares!
import random
n = int(input("Informe a quantidade de linhas da matriz: "))
m = int(input("Informe a quantidade de colunas da matriz: "))
pares = 0
matriz = []

for linha in range(n):
    lista = []
    for coluna in range(m): 
        sorteado = random.randint(1,100)
        if (sorteado % 2) == 0:
            pares += 1
        lista.append(sorteado)
    matriz.append(lista)

print("MATRIZ")
for linha in range(n):
    for coluna in range(m):
        print (matriz[linha][coluna], end = "\t")
    print ()
print ("-"*40)
print(f"A quantidade de números pares é {pares}")
