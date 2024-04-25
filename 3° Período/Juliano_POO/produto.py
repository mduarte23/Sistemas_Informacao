class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome= nome
        self.preco = preco
        self.quantidade = quantidade

    def mostra_info(self):
        print (f'Nome: {self.nome}')
        print (f'Preco: {self.preco}')
        print (f'Quantidade: {self.quantidade}')

    def mostra_valor_estoque(self):
        print (f"Valor total do estoque: R${self.preco * self.quantidade}")

print (f'='*30)   
produto1 = Produto('água', 1.99, 20)
produto1.mostra_info()
produto1.mostra_valor_estoque()
print (f'='*30)
produto2 = Produto('refrigerante', 4.99, 25)
produto2.mostra_info()
produto2.mostra_valor_estoque()
print (f'='*30)