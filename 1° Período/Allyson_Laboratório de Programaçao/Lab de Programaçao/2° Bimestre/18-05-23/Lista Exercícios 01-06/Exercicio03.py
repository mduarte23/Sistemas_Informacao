# 3- Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

for numeros in range (1,21):
    print (numeros)

print ('=' * 10)

for numeros in range (1,21):
    if numeros == 20:
        print (numeros)
    else:
        print (numeros, end=(', '))
