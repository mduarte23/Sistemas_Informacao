from class_conta import Conta
from class_cliente import Cliente

#Cliente
nome = str(input("Informe o nome: "))
cpf = int(input("Informe o CPF (números): "))
idade = int(input("Informe a idade: "))
rg = int(input("Informe o RG"))

usuario1 = Cliente(nome,cpf, idade, rg)

#Conta
num_conta = str(input("A respeito de sua conta, informe o número da mesma: "))
saldo = float(input("Informe seu saldo: "))

conta1 = Conta(usuario1, num_conta, saldo)

print (f"Seja bem-vindo(a) {usuario1.nome}, de conta número {conta1.num_conta}.")


respondendo = True

while respondendo:
    opcao = int(input("\n"'''O que deseja fazer?
    1 - Saque
    2 - Depósito
    3 - Saldo
    4 - Meu Dados
    5 - Sair
                      
Opcao: '''))
    
    if opcao == 1:
        valor = float(input(f"Quando deseja sacar do seu saldo de R${conta1.saldo}? "))
        conta1.saque(valor)
    elif opcao == 2:
        valor = float(input(f"Quanto deseja depositar? "))
        conta1.deposito(valor)
    elif opcao == 3:
        conta1.mostrar_saldo()
    elif opcao == 4:
        usuario1.mostrar_dados()
    elif opcao == 5:
        print ("Obrigado! Até a próxima.")
        respondendo = False
    else:
        print("Opção inválida, tente novamente.")