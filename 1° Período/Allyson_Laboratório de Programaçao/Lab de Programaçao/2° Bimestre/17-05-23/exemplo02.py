"""Faça um  programa para determinar o número de dígitos de um número interio positivo informado
ex: entrada: 20342 saída: tem 5 digitos
    entrada: 2034 saída: tem 4 digitos
    entrada: -3524 saída: número invalido"""
contador = 0
numero= int(input('Digite o número: '))
if numero > 0:
    while numero != 0:
        numero = numero // 10
        contador+=1
    print (f'O número tem {contador} dígitos.')
else:
    print(f'O número {numero} é inválido.')