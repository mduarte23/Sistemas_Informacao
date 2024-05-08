class Conta:
    def __init__(self, cliente, num_conta, saldo):
        self.cliente = cliente
        self.num_conta = num_conta
        self.saldo = saldo

    def saque(self, valor):
        if valor > self.saldo:
            print ("\nNão foi possivel realizar a operação. Valor maior que o disponível em conta")
        else:
            self.saldo -= valor
            print (f'\nO valor de R${valor} foi sacado, novo saldo: R${self.saldo}')

    def deposito(self,valor):
        if valor < 0 or valor == 0:
            print (f"\nNão foi possivel realizar a operação. Valor inválido ou insuficiente")
        else:
            self.saldo += valor
            print (f'\nO valor de R${valor} foi depositado, novo saldo: R${self.saldo}')

    def mostrar_saldo(self):
        print (f"\nO seu saldo atual é de R${self.saldo}")