"""
Programa que imprime a soma de todos os números pares entre dois números quaisquer, incluindo-os .
"""

numero1=int(input('Digite o primeiro número: '))
numero2=int(input('Digite o segundo número: '))
soma = 0

while numero1 > numero2:
    print('Primeiro número deve ser o menor, tente novamente:')
    numero1=int(input('Digite o primeiro número: '))
    numero2=int(input('Digite o segundo número: '))

for i in range (numero1,numero2+1):
    if i % 2 == 0:
        print (i)
        soma = soma + i
print (f'A soma dos pares no intervalo entre os numeros {numero1} e {numero2} é {soma}')