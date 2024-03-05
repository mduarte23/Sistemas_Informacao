#Identificar se o número é par
numero = int (input('Digite o valor: '))

resto = numero % 2

if resto == 0:
    print(f'{numero} é par!!!')
else:
    print(f'{numero} é impar!!!')

print ('Fim da execução')

