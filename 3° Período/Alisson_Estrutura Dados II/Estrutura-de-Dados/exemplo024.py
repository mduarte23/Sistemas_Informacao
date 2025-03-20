import random
def calcula_media(v):
    """Função que calcula a media dos valores de uma lista"""
    if len(v) > 0:
        return sum(v)/len(v)
    else:
        return 0
   
def menu():
    """Funçao que cria um menu""" 
    print("="*10)
    print('1 - Iniciar lista aleatória')
    print("2 - Calcular media")
    print('3 - Pesquisar valor')
    print("4 - Sair")
    return int(input("Digite sua opção: "))

def inicializa_lista(quantidade = 5): #se passar a quantidade ele muda a quantidade, senão utiliza o 5
    """Cria uma lista aleatória"""
    lista = []
    for _ in range(quantidade):
        valor = random.randint(0,100)
        lista.append(valor)
    return lista

def pesquisar():
    p= int(input("Digite o valor que deseja pesquisar: "))
    return p in v
   
if __name__ == '__main__':
    v = []
    op = 0
    while op != 4:
        op = menu()
        if op == 1:
            v = inicializa_lista()
            print(v)
        elif op == 2:
            media = calcula_media(v)
            print(f"A média é {media:.2f}")
        elif op == 3:
            pesquisa = pesquisar()
            if pesquisa == True:
                print("Está Presente")
            else:
                print("Não está presente")
    else:
        print("Saindo...")
    
    

