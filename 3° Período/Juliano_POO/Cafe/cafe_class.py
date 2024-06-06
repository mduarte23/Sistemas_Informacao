class Cafe:
    #construtor
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco = float(preco)

    def check_orcamento(self, orcamento):
        #Checa se o orcamento é valido
        if not isinstance(orcamento, (int, float)):
            print ("Digite float ou int")
            exit()
        if orcamento < 5:
            print("Desculpe, você não tem dinheiro")

    def get_change(self, orcamento):
        return orcamento - self.preco
    
    def vender(self, orcameto):
        self.check_orcamento(orcamento)
        if orcameto >= self.preco:
            print(f'Você pode comprar o {self.nome} café')
            if orcamento == self.preco:
                print ("Valor exato")
            else:
                print (f"Aqui está seu troco R${self.get_change(orcamento)}")

            exit("Obrigado pela sua compra")
