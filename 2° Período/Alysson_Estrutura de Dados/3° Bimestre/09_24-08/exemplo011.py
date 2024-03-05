opcao = 1
bd_estoque = []
while opcao != 4:
    print ('='*20)
    print("1 - Adicionar")
    print('2 - Consultar Estoque')
    print('3 - Consultar valor do estoque')
    print('4 - Sair')
    opcao = int(input('Opção >>>>> '))
    if opcao == 1:
        print('-----Adicionar produto-----')
        codigo = int(input("Código: "))
        nome = input('Nome: ')
        descricao = input('Descrição: ')
        preco = float(input('Preço: R$'))
        quantidade = int(input('Quantidade: '))
        produto =[codigo, nome, descricao, preco, quantidade]
        bd_estoque.append(produto)
        print("-----Produto adicionado com sucesso-----")
    elif opcao == 2:
        print ('-----Estoque-----')
        print ('Código\tNome\tDescrição\tPreço\tQuantidade')
        for prod in bd_estoque:
            print(prod[0], end='\t')
            print(prod[1], end='\t')
            print(prod[2], end='\t')
            print(prod[3], end='\t')
            print(prod[4])
        print("-----Fim do estoque-----")
    elif opcao == 3:
        print('-----Valor total do estoque-----')
        total = 0
        for prod in bd_estoque: 
            soma = prod[3] * prod[4]
            total = total + soma
        print (f'-----R${total:.2f}-----')
    elif opcao == 4:
        print('-----Sair-----')
    else:
        print('Opçao incorreta')
