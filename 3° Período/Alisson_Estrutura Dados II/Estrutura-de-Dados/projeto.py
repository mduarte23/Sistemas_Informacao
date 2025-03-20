"""
produto - fruta
atributos: nome, código, preço, peso
chave: código
valor: nome, preço, peso
"""
import json


banco_dados = {}
opcao = 1
#carregar o que está no arquivo
try: #tente
    with open("12_05-09/Base_Dados/estoque.json", "r") as arquivo:
        banco_dados = json.load(arquivo)
except: #se não existir
    print('O arquivo não existe')
  
while opcao != 7:
    print("="*10)
    print("1-Adicionar")
    print("2-Consultar por código") 
    print("3-Consultar todos produtos")
    print("4-Alterar o preço do produto")
    print("5-Aplicar desconto")
    print("6-Excluir produto")
    print("7-Sair")
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        print("-"*10)
        print('CADASTRO')
        codigo = input('Digite o código: ').upper() #coloca todas letras maiusculas
        while codigo in banco_dados: #verifica se o código já existe
            codigo = input('Código ja existe, tente outro código: ').upper()
        nome = input("Digite o nome do produto: ")
        preco = float(input('Digite o preço do Kg/unidade: '))
        qtd = float(input("Digite a quantidade: "))
        if qtd > 0: 
            disponivel = True
        else:
            disponivel = False
        banco_dados[codigo] = {"Nome": nome, "Preco": preco, "Quantidade": qtd, "Disponivel": disponivel}
        with open("12_05-09/Base_Dados/estoque.json", "w") as arquivo:
            json.dump(banco_dados, arquivo, indent=4)
    elif opcao == 2:
        print("-"*10)
        print('CONSULTAR POR CÓDIGO')
        cod = input('Informe o código que deseja consultar: ').upper()
        while cod not in banco_dados: #verifica se o código esta no banco de dados
            cod = input('Código não existe, tente novamente: ').upper()
        print ('Código\t\tNome\t\tPreço\t\tQuantidade\tDisponível')
        print(cod, end="\t\t")
        if len(banco_dados[cod]["Nome"]) > 7: #verifica o tamanho do "Nome", se for mairo que 7 imprime com 2 tabulaçoes
            print (banco_dados[cod]["Nome"], end="\t")
        else:
            print (banco_dados[cod]["Nome"], end="\t\t")
        print (f'{banco_dados[cod]["Preco"]:.2f}', end="\t\t")
        print (banco_dados[cod]["Quantidade"], end="\t\t")
        print (banco_dados[cod]["Disponivel"])
            
    elif opcao == 3:
        print("-"*10)
        print('CONSULTAR TODOS')
        print ('Código\t\tNome\t\tPreço\t\tQuantidade\tDisponível')
        for chave in banco_dados: # percorre o banco_dados
            produto = banco_dados[chave]
            print (chave, end="\t\t")
            if len(produto["Nome"]) > 7:
                print (produto["Nome"], end="\t")
            else:
                print (produto["Nome"], end="\t\t")
            print (f'{produto["Preco"]:.2f}', end="\t\t")
            print (produto["Quantidade"], end="\t\t")
            print (produto["Disponivel"])
      
    elif opcao == 4:
        print("-"*10)
        print('ALTERAR PREÇO')
        cod = input('Informe o código do produto que deseja alterar: ').upper()
        if cod not in banco_dados: #verifica se o codigo esta no banco de dados
            cod= input("Codigo inexistente, tente novamente: ")
        else:
            novo_preco = float(input("Informe o novo preço: "))
            banco_dados[cod]["Preco"] = novo_preco #altera o preco do produto selecionado
            with open("12_05-09/Base_Dados/estoque.json", "w") as arquivo:
                json.dump(banco_dados, arquivo, indent=4)
        
    elif opcao == 5:
        print("-"*10)
        print('ALTERAR PREÇO')
        print("-"*10)
        #sub menu
        print('1-Adicionar')
        print('2-Desconto')
        print('3-Retornar ao menu')
        alterar= int(input('Deseja adicionar ou descontar?: '))
        if alterar == 1: 
            porcentagem = float(input('Qual a porcentagem de acréscimo: '))
            for i in banco_dados:
                banco_dados[i]["Preco"]= (banco_dados[i]["Preco"] * (porcentagem / 100)) + banco_dados[i]["Preco"]
        elif alterar == 2:
            porcentagem = float(input('Qual a porcentagem de desconto: '))
            for i in banco_dados:
                banco_dados[i]["Preco"]= banco_dados[i]["Preco"] - (banco_dados[i]["Preco"] * (porcentagem / 100))
        elif alterar == 3: #retorna ao menu principal
            opcao == 1
        else:
            alterar = int(input("Opção invalida, tente novamente: "))
        with open("12_05-09/Base_Dados/estoque.json", "w") as arquivo:
            json.dump(banco_dados, arquivo, indent=4)
        print('Preço alterado.')
    elif opcao == 6:
        print("-"*10)
        print('EXCLUIR PRODUTO')
        cod = input("Informe o código do produto que deseja excluir: ").upper()
        if cod not in banco_dados: #verifica se o codigo esta no banco_dados
            cod= input('Código inexistente, tente novamente: ')
        else:
            del banco_dados[cod] #exclui o produto pelo codigo
            print('Produto excluido')
            with open("12_05-09/Base_Dados/estoque.json", "w") as arquivo:
                json.dump(banco_dados, arquivo, indent=4)
        
    elif opcao == 7:
        print ("-"*10)
        print ("SAIR")
          
    else:
        print("-"*10)
        print('OPÇÃO INVÁLIDA')