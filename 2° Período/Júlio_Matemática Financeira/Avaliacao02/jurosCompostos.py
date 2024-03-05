import math
opcao = 0
while opcao != 5:
    print("CALCULO DE JUROS COMPOSTOS")
    print("1-Descobrir o Montante")
    print("2-Descobrir o Capital")
    print("3-Descobrir a Taxa")
    print("4-Descobrir o Tempo")
    opcao = int(input("Escolha a opção: "))
    
    if opcao == 1:
        print("DESCOBRIR MONTANTE")
        capital = float(input("Digite o Capital: "))
        taxa = float(input("Digite a porcentagem de Taxa ao mês: "))
        tempo = float(input("Digite o tempo em meses: "))
        montante = capital * (1 + (taxa/100))**tempo
        print(f"O Montante é R${montante:.2f}")
    elif opcao == 2:
        print("DESCOBRIR CAPITAL")
        montante = float(input("Digite o Montante: "))
        taxa = float(input("Digite a porcentagem de taxa ao mês: "))
        tempo = float(input("Digite o tempo em meses: "))
        parentese = (1 + taxa)**tempo
        capital = montante / parentese
        print(f'O Capital é R${capital:.2f}')
    elif opcao == 3:
        print("DESCOBRIR TAXA")
        montante = float(input("Digite o Montante: "))
        capital = float(input("Digite o Capital: "))
        tempo = float(input("Digite o tempo em meses: "))
        divisao = montante / capital
        raiz = divisao **(1 / tempo)
        taxa = (raiz - 1) * 100
        print(f'A taxa é {taxa:.2f}% a.m. ')
    elif opcao == 4:
        print("DESCOBRIR TEMPO")
        montante = float(input('Digite o Montante: '))
        capital = float(input("Digite o Capital: "))
        taxa = float(input("Digite a porcentagem de Taxa ao mês: "))
        divisao = montante / capital
        tempo = math.log(divisao) / math.log(1 + (taxa / 100))
        print (f"O Tempo é de {tempo:.2f} meses")
    elif opcao == 5:
        print ("SAIR")
    else:
        opcao = int(input("Opção inválida, tente novamente: "))