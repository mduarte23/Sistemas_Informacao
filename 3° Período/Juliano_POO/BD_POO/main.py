from class_bancodados import BancoDados
from class_cliente import Cliente

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    novo_cliente = Cliente(nome, email, telefone)

    BancoDados.inserir(novo_cliente)

    print("Cliente cadastrado com sucesso")

def listar_clientes():
    clientes = BancoDados.listar_clientes()
    for cliente in clientes:
        print (f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | Telefone: {cliente[3]}")

def atualizar_cliente():
    cliente_id = int(input("Digite o ID do cliente a ser atualizado: "))
    novo_nome = input("Digite o novo nome do cliente: ")
    novo_email = input("Digite o novo email do cliente: ")
    novo_telefone = input("Digite o novo telefone do cliente: ")

    cliente_atualizado = Cliente(cliente_id, novo_nome, novo_email, novo_telefone)

    BancoDados.atualizar_cliente(cliente_atualizado)
    print("Cliente atualizado com sucesso!")

def deletar_cliente():
    cliente_id = int(input("Digite o ID do cliente a ser excluido: "))
    BancoDados.deletar_cliente(cliente_id)
    print ("Cliente deletado com sucesso!")
