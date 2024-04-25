class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email= email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print('Plano inválido')
            #raise Exception ("Plano inválido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano Inválido')
    
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print (f"Ver filme {filme}")
        elif self.plano == 'premium':
            print (f'Ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print ('Faça um upgrade para ver o filme')
        else:
            print ('Plano inválido')


cliente = Cliente('Marcelo', 'marceloduarte@ns.net.br', 'basic')
print (cliente.nome)
print (cliente.plano)
cliente.ver_filme("Harry Potter", "premium")

cliente .mudar_plano('premium')
print (cliente.plano)
cliente.ver_filme("Harry Potter", "premium")