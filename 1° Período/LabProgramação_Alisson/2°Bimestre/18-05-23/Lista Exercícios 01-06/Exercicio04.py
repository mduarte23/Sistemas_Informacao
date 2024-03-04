# 4- Faça um programa, utilizando while, que mostre na tela os números de  0 a 100.

numero = 0 
print (numero, end=(', '))
while numero < 100:
    numero +=1
    if numero == 100:
        print (numero)
    else:
        print (numero, end=(', '))