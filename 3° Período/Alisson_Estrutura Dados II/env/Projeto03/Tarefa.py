class Tarefa():
    #construtor
    def __init__(self, titulo: str):
        #print ("Construtor")
        #__ declara como privado
        self.__tit = titulo
        #define o valor da prioridade como o tamanho do titulo
        self.__prioridade = len(self.__tit)
        self.__desc = "--"

    def get_titulo(self):
        return self.__tit
    
    def get_descricao (self):
        return self.__desc
    
    def get_prioridade(self):
        return  self.__prioridade
    
    def set_descricao(self, descricao: str):
        self.__desc = descricao

    def info(self):
        return f"Titulo: {self.__tit}\nDescrição: {self.get_descricao()}\nPrioridade: {self.get_prioridade()}"

    