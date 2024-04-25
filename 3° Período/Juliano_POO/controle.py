class ControleRemoto:
    #abrindo construtor
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    #criando um parametro
    
    def trocar_canal(self, botao):
        if botao == ">":
            print ("Avança canal")
        elif botao == "<":
            print ("Volta canal")

controle_remoto = ControleRemoto("Branco", "10cm", "2cm", '4cm')
print(controle_remoto.cor)



controle_remoto2 = ControleRemoto("Preto", "12cm", "2cm", '3cm')
print(controle_remoto2.cor)

apertar = input("Precione o botao: ")
#chama a funcão e parametro
controle_remoto.trocar_canal(apertar)