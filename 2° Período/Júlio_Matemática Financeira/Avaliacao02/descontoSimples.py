opcao = 0
while opcao != 6:
    print("DESCONTO SIMPLES")
    print("1-Descobrir o Desconto")
    print("2-Descobrir o valor Nominal")
    print("3-Decobrir o valor Atual")
    print("4-Descobrir a Taxa")
    print("5-Descobrir o Tempo")
    print("6-Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("DESCOBRIR O DESCONTO")
        n = float(input("Informe o valor nominal: "))
        i = float(input("Informa a porcentagem da taxa mensal: "))
        t = float(input("Informe o tempo: "))
        d = n * (i / 100) * t
        print(f'O valor do desconto é R${d:.2f}')
    elif opcao == 2:
        print("DESCOBRIR O VALOR NOMINAL")
        a = float(input("Informe o valor atual: "))
        i = float(input("Informe a porcentagem da taxa mensal: "))
        t = float((input("Informe o tempo em meses: ")))
        n = a / (1 - ((i / 100) * t))
        print(f'O valor nominal é R${n:.2f}')
    elif opcao == 3:
        print("DESCOBRIR O VALOR ATUAL")
        n = float(input("Informe o valor nominal: "))
        i = float(input("Informe a porcentagem da taxa mensal: "))
        t = float(input("Informe o tempo em meses: "))
        a = n * (1 - (i / 100) * t)
        print(f"O valor atual é R${a:.2f}")
    elif opcao == 4:
        print("DESCOBRIR A TAXA")
        d = float(input("Informe o desconto: "))
        n = float(input("Informe o valor nominal: "))
        t = float(input("Informe o tempo em meses: "))
        i = (d / (n * t)) * 100
        print(f'A taxa mensal é de {i:.2f}% a.m.')
    elif opcao == 5:
        print("DESCOBRIR O TEMPO")
        d = float(input("Informe o desconto: "))
        n = float(input("Informe o valor nominal: "))
        i = float(input("Informe a porcentagem da taxa mensal: "))
        t = d / (n * (i / 100))
        print(f"O tempo é de {t:.2f} meses")
    elif opcao == 6:
        print("SAIR")
    else:
        opcao = int(input("Opção inválida, tente novamente: "))