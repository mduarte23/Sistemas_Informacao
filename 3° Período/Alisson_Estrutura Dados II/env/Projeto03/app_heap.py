from Tarefa import Tarefa
import heapq

lista_tarefas = []

def menu():
    print ("-"*10)
    print ("1- Adicionar Tarefa")
    print ("2- Realizar Tarefa (remover)")
    print ("3- Consultar Tarefas")
    print ("4- Sair")

def adicionar():
    titulo = input("Digite o titulo: ")
    descricao = input ("Digite a descrição: ")

    obj = Tarefa(titulo)
    obj.set_descricao(descricao)
    prioridade = obj.get_prioridade()
    heapq.heappush(lista_tarefas, (1/prioridade, obj))

def realizar():
    if len(lista_tarefas) > 0:
        #devolve a tarefa de maior prioridade
        print ("Lista esta vazia")


def consultar():
    for item in lista_tarefas:
        print (item[1].info())
        print ("-"*10)

if __name__ == "__main__":
    opcao = 1
    while opcao != 4:
        menu()
        opcao = int (input("Digite a opção: "))
        if opcao == 1:
            adicionar()
        elif opcao == 2:
            realizar()
        elif opcao == 3:
            consultar()
        elif opcao == 4:
            print ("Saindo")
        else:
            print("Opção inválida: ")
    