opcao = input('digite (S) para somar ou (M) para multiplicar: ')

if opcao == 'S' or opcao == 'M':
    numero1 = float(input('Digite o 1° numero: '))
    numero2 = float(input('Digite o 2° numero: '))

if opcao == 'S':
    resultado = numero1 + numero2
    print (f'O resultao da soma é {resultado}')
elif opcao == 'F':
    resultado = numero1 * numero2
    print (f'O resultado da multiplicação é {resultado}')
else:
    print('Opção invalida!')
print('Fim da operação!!!')