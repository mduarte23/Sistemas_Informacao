opcao = input('Para SOMAR digite "S" ou para MULTIPLICAR digite "M": ')
opcao = opcao.strip().upper() #upper: converte letra minuscula para maiuscula .strip elimina espaço
if (opcao== 'S' or opcao == 'M'): 
    x= float (input('Digite o valor de x: '))
    y = float (input('Digite o valor de y: '))
    if opcao == 'S':
        r = x + y
    else:
        r = x * y
    print(f'O resultado é {r}')
else:
    print ('Opção inválida!')      