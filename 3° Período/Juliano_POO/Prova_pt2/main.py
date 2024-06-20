from class_BancoDados import BancoDados
from class_filme import Filme 
def cadastrar_filme():
    titulo = input("Digite o título do filme: ")
    ano = input("Digite o ano do filme: ")
    genero = input("Digite o genero do filme: ")
    runtime = input("Digite o runtime do filme: ")
    diretor = input("Digite o nome do diretor do filme: ")
    novo_filme = Filme(titulo, ano, genero, runtime, diretor)
    Banco_Dados.inserir_filme(novo_filme)
    print("Filme cadastrado com sucesso!")

def listar_filmes():
    filmes = Banco_Dados.listar_filmes()
    for filme in filmes:
        print(f"ID: {filme[0]} | Título: {filme[1]} | Ano: {filme[2]} | Gênero: {filme[3]} | Runtime: {filme[4]} | Diretor: {filme[5]}")

def atualizar_filme():
    filme_id = int(input("Digite o ID do filme a ser atualizado: "))
    novo_titulo = input("Digite o novo título do filme: ")
    novo_ano = input("Digite o novo ano do filme: ")
    novo_genero = input("Digite o novo gênero do filme: ")
    novo_runtime = input("Digite o novo runtime do filme: ")
    novo_diretor = input("Digite o novo diretor do filme: ")
    filme_atualizado = Filme( novo_titulo, novo_ano, novo_genero, novo_runtime, novo_diretor)
    Banco_Dados.atualizar_filme(filme_atualizado, filme_id)
    print("Filme atualizado com sucesso!")

def deletar_filme():
    filme_id = int(input("Digite o ID do filme a ser deletado: "))
    Banco_Dados.deletar_filme(filme_id)
    print("Filme deletado com sucesso!")

Banco_Dados = BancoDados()

while True:
    print("\nMenu Principal:")
    print("1. Cadastrar Filme")
    print("2. Listar Filmes")
    print("3. Atualizar Filme")
    print("4. Deletar Filme")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        cadastrar_filme()
    elif opcao == '2':
        listar_filmes()
    elif opcao == '3':
        atualizar_filme()
    elif opcao == '4':
        deletar_filme()
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")

Banco_Dados.conexao.close()  # Fechar a conexão com o banco de dados