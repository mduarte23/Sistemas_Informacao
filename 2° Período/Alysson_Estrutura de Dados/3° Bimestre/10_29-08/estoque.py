estoque = {} #DICIOÁRIO
opcao = 1
while opcao != 3:
    print ("-" * 10)
    print ('---MENU---')
    print ('1-Adicionar')
    print ('2-Consultar')
    print ('3-Sair')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        codigo = input('Código: ')
        nome = input('Produto: ')
        estoque[codigo] = nome
        print ('Adicionado com sucesso')
    elif opcao == 2:
        codigo = input('Código desejado: ')
        if codigo in estoque:
            registro = estoque[codigo]
            print (f'Registo Recuperado: {registro}')
        else:
            codigo = input('Codigo inextente, tente novamente: ')
    elif opcao == 3:
        print ('Saindo...')
               
        
