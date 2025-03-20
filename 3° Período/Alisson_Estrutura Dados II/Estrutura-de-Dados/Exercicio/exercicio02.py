#2- Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um
#número k. Imprima a matriz na tela antes e depois da multiplicação.
#ex:     
#input
#|  4     6    9 |
#|  3     2    7 |
#|  1     2    5 |

#ouput, suponha k = 5
#|  20     6     9 |
#|  3       10    7 |
#|  1     2      25 |
def multiplicar(x,y):
    resultado = x * y
    return resultado


import random
matriz = []
linha = 3
coluna = 3
k = int(input("Informe o número que deseja multiplicar diagonal principal da matriz: "))

for lin in range(linha):
    lista = []
    for col in range(coluna):
        numero = random.randint(1,99)
        lista.append(numero)
    matriz.append(lista)

print ("Matriz Original")

for l in range(linha):
    for m in range(coluna):
        print (matriz[l][m], end = "\t")
    print()

print (f"Matriz com a diagonal principal multiplicada por {k}")
matriz[0][0] = multiplicar(matriz[0][0], k)
matriz[1][1] = multiplicar(matriz[1][1], k)
matriz[2][2] = multiplicar(matriz[2][2], k)

for l in range(linha):
    for m in range(coluna):
        print (matriz[l][m], end = "\t")
    print()