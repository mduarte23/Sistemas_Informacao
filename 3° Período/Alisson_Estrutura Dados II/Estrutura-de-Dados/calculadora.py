"""Faça uma calculadora que forneça as seguintes opções para o usuário, usando funções sempre que necessário. Cada opção deve usar como operando um número lido do teclado e o valor atual da memória. Por exemplo, se o estado atual da memória é 5, e o usuário escolhe somar, ele deve informar um novo número (por exemplo, 3). Após a conclusão da soma, o novo estado da memória passa a ser 8.

Estado da memória: 0
Opções:
(1) Somar
(2) Subtrair
(3) Multiplicar
(4) Dividir
(5) Limpar memória
(6) Sair do programa
Qual opção você deseja?"""

import os

def menu():
    "Funçao que vai chamar o menu"
    os.system('cls')
    print ("="*30)
    print(f"Memoria: {memoria}")
    print("1-Somar")
    print ("2-Subtrair")
    print ("3-Multiplicar")
    print ("4-Dividir")
    print ("5-Limpar Memória")
    print ("6-Sair")
    op = int(input("Informe a opção: "))
    while op < 1 or op > 6:
        op = int(input("Opção inválida, tente novamente: "))
    return op
    

def somar(a, b):
    return a + b

def subtrair (a, b):
    return a - b

def multiplicar (a, b):
    return a * b

def dividir (a, b):
    return a / b

def limpar():
    return 0

if __name__ == '__main__':
    memoria = 0
    opcao = 0
    while opcao != 6:
        opcao = menu()
        if opcao == 1 :
            print ("-----SOMANDO-----")
            soma = int(input(f"Digite o número que deseja somar a {memoria}: "))
            memoria = somar(memoria, soma)
        
        elif opcao == 2:
            print ("-----SUBTRAINDO-----")
            subtracao = int(input(f"Digite o número que deseja subtrair de {memoria}: "))
            memoria = subtrair(memoria, subtracao)


        elif opcao == 3:
            print ("-----MULTIPLICANDO-----")
            multiplicacao = int(input(f"Digite o número que deseja multiplicar por {memoria}: "))
            memoria = multiplicar(memoria, multiplicacao)

        elif opcao == 4:
            print ("-----DIVIDINDO-----")
            divisao = int(input(f"Digite o número que deseja dividir por {memoria}: "))
            memoria = dividir(memoria, divisao)


        elif opcao == 5:
            print ("-----LIMPANDO MEMÓRIA-----")    
            memoria = limpar()

        elif opcao == 6:
            print('-----SAINDO-----')

       