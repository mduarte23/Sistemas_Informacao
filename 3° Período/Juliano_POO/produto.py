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


class ProdutoPerecivel(Produto):
    def __init__(self, nome, preco, quantidade, data_validade):
        super().__init__(nome, preco, quantidade)
        self.data_validade = data_validade
    
    def mostrar_validade(self):
        print (f'O produto vence no dia {self.data_validade}')

    def mostra_info(self):
        super().mostra_info()
        print ('-'*30)
        print (f'O produto {self.nome} é perecível')
        print ('-'*30)


print (f'='*30)   
produto1 = Produto('água', 1.99, 20)
produto1.mostra_info()
produto1.mostra_valor_estoque()
print (f'='*30)

produto2 = Produto('refrigerante', 4.99, 25)
produto2.mostra_info()
produto2.mostra_valor_estoque()
print (f'='*30)

produto3 = ProdutoPerecivel('leite', 7.99, 10, '10/05/2024')
produto3.mostra_info()
produto3.mostra_valor_estoque()
produto3.mostrar_validade()
print (f'='*30)

produto4 = ProdutoPerecivel('maça', 0.99, 15, '05/05/2024')
produto4.mostra_info()
produto4.mostra_valor_estoque()
produto4.mostrar_validade()
print (f'='*30)

carrinho_produtos = [Produto('água', 1.99, 20),
                    Produto('refrigerante', 4.99, 25), 
                    ProdutoPerecivel('leite', 7.99, 10, '10/05/2024'), 
                    ProdutoPerecivel('maça', 0.99, 15, '05/05/2024')]

for i in carrinho_produtos:
    i.mostra_info()
    print ('='*40)
