from Tarefa import Tarefa

obj = Tarefa("Lavar roupa")
outro = Tarefa("Fazer almoço")
outro.set_descricao("Descrição adicionada")

print (obj.info())
print (f"-"*30)
print (outro.info())
