opcao = 0
while opcao != 5: 
    print ("1-Descobrir o Juros")
    print ("2-Descobrir o Capital")
    print("3-Descobrir o Tempo")
    print("4-Descobrir a Taxa")
    print("5-Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        print('-'*30)
        print("Descobrir o Juros")
        capital = float(input("Digite o Capital: "))
        tempo = float(input("Digite o tempo em meses: "))
        taxa = float(input("Digite a taxa mensal em porcentagem: "))
        juros = capital * (taxa / 100) * tempo
        montante = juros + capital
        print(f'O juros é R${juros:.2f}')
        print(f'O Montante é R${montante:.2f}')
    elif opcao == 2:
        print('-'*30)
        print("Descobrir o Capital")
        juros = float(input('Digite o juros: '))
        tempo = float(input("Digite o tempo em meses: "))
        taxa = float(input("Digite a taxa mensal em porcentagem: "))
        capital = juros / ((taxa / 100) * tempo)
        montante = capital + juros
        print(f"O Capital é R${capital:.2f}")
        print(f"O montante é R${montante:.2f}")
    elif opcao == 3:
        print('-'*30)
        print("Descobrir o Tempo")
        juros = float(input("Digite o Juros: "))
        capital = float(input("Digite o Capital: "))
        taxa = float(input("Digite a taxa mensal em porcentagem: "))
        tempo = juros / (capital * (taxa / 100))
        montante = capital + juros
        print (f'O tempo é {tempo} meses')
        print (f'O montante é R${montante:.2f}')
    elif opcao == 4:
        print('-'*30)
        print("Descobrir a Taxa")
        juros = float(input("Digite o Juros: "))
        capital = float(input("Digite o Capital: "))
        tempo = float(input("Digite o tempo em meses: "))
        taxa = (juros / (capital * tempo)) * 100
        montante = capital + juros
        print (f'A taxa de juros é {taxa:.2f}% a.m.')
        print(f"O montante é R${montante:.2f}")
    elif opcao == 5:
        print('-'*30)
        print("SAIR")
    else:
        opcao = int(input("Opção inválida, tente novamente: "))

