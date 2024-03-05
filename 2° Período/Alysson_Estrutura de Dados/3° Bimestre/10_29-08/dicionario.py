clientes = {} # {} representa que é um dicionario

clientes['000.000.000-00'] = ['Joaquim', 20] #adiciona nome e idade no cpf
clientes["111.111.111-11"] = 'Tereza' 
print (clientes)

#recuperar apenas o registro com cpf 111.111.111-11
nome = clientes['111.111.111-11']
print(nome)

#recuperar apenas o registro com cpf 000.000.000-00
valor = clientes['000.000.000-00']
print(valor)

chaves = clientes.keys() #retorna apenas as chaves
print (chaves)

for cpf in clientes.keys():
    print (f'CPF: {cpf}')
    valor= clientes[cpf]
    print(valor)

#outra forma de criar um dicionário
produtos = {'mouse': {'cor': 'preto', 'preco': 65.99}, 'teclado':{'cor': 'branco', 'preco':70}}
print (produtos)

print(produtos['mouse'] ['cor'])
