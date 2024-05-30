from class_bd_empresa import BancoDados
from class_empresa import Empresa

def cadastrar_empresa():
    nome = input("Digite o nome da empresa: ")
    endereco = input("Digite o endereco da empresa: ")
    contato = input("Digite o contato da empresa: ")
    ramo = input("Digite o ramo da empresa: ")
    telefone = input("Digite o telefone do cliente: ")

    nova_empresa = Empresa(nome, endereco, contato, ramo, telefone)

    Banco_Dados.inserir_empresa(nova_empresa)

    print("Empresa cadastrada com sucesso")

def listar_empresas():
    empresas = Banco_Dados.listar_empresas()
    for empresa in empresas:
        print (f"ID: {empresa[0]} | Nome: {empresa[1]} | Endereco: {empresa[2]} | Contato: {empresa[3]} | Ramo: {empresa[4]} | Telefone: {empresa[5]}")

def atualizar_empresa():
    empresa_id = int(input("Digite o ID da empresa a ser atualizada: "))
    novo_nome = input("Digite o novo nome da empresa: ")
    novo_endereco = input("Digite o novo endereco da empresa: ")
    novo_contato = input("Digite o novo contato da empresa: ")
    novo_ramo = input("Digite o novo ramo da empresa: ")
    novo_telefone = input("Digite o novo telefone da empresa: ")

    empresa_atualizada = Empresa(novo_nome, novo_endereco, novo_contato, novo_ramo, novo_telefone)

    Banco_Dados.atualizar_empresa(empresa_atualizada, empresa_id)
    print("Empresa atualizada com sucesso!")

def deletar_empresa():
    empresa_id = int(input("Digite o ID da empresa a ser excluida: "))
    Banco_Dados.deletar_empresa(empresa_id)
    print ("Empresa deletada com sucesso!")


Banco_Dados = BancoDados()

while True:
    print ("\nMenu Principal:")
    print ("1- Cadastrar Empresa")
    print ("2- Listar Empresas")
    print ("3- Atualizar Empresa")
    print ("4- Deletar Empresa")
    print ("0- Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        cadastrar_empresa()
    elif opcao == '2':
        listar_empresas()
    elif opcao == '3':
        atualizar_empresa()
    elif opcao == '4':
        deletar_empresa()
    elif opcao == '0':
        print ("Saindo...")
        break
    else: 
        print("Opção inválida!")

#fechar a conexao com o banco de dados
Banco_Dados.conexao.close()
