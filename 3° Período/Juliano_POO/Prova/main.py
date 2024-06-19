from class_operadores import Operadores

def somar():
    valor1 = float(input("Escolha o valor 1: "))
    valor2 = float(input("Escolha o valor 2: "))
    numeros = Operadores(valor1, valor2)
    print (Operadores.soma(numeros))

def subtrair():
    valor1 = float(input("Escolha o valor 1: "))
    valor2 = float(input("Escolha o valor 2: "))
    numeros = Operadores(valor1, valor2)
    print (Operadores.subtracao(numeros))

def multiplicar():
    valor1 = float(input("Escolha o valor 1: "))
    valor2 = float(input("Escolha o valor 2: "))
    numeros = Operadores(valor1, valor2)
    print (Operadores.multiplicacao(numeros))

def dividir():
    valor1 = float(input("Escolha o valor 1: "))
    valor2 = float(input("Escolha o valor 2: "))
    numeros = Operadores(valor1, valor2)
    print (Operadores.divisao(numeros))

while True:
    print("-------CALCULADORA-------")
    print("1- Adição")
    print("2- Subtração")
    print("3- Divisão")
    print("4- Multiplicação")
    print("0- Sair")
    print("--------------------------")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        somar()
    elif opcao == "2":
        subtrair()
    elif opcao == "3":
        dividir()
    elif opcao == "4":
        multiplicar()
    elif opcao == "0":
        print ("Saindo...")
        break
    else:
        print("Opcão inválida")