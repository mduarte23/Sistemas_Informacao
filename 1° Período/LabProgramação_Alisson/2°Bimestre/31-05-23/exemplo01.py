nome = "Maria Silva"
tamanho = len(nome) #len devolve o comprimento da String
for indice in range(tamanho):
    letra = nome[indice]
    print(f'{indice} = {letra}')

chave = 'a'
if chave in nome: #Pesquisa na string se a letra esta presente
    print(f'{chave} ESTÁ presente em {nome}')
else:
    print(f'{chave} NÃO ESTÁ presente em {nome}')

if chave not in nome:
    print(f'{chave} NÃO ESTÁ presente em {nome}')
else:
    print(f'{chave} ESTÁ presente em {nome}')

# + operador de contatenação -> juntar
primeiro_nome = 'Alan'
sobrenome = 'Turing'
nome_completo = primeiro_nome + sobrenome
print (nome_completo)

primeiro_nome = 'Alan'
sobrenome = 'Bida'
nome_completo = primeiro_nome + ' ' + sobrenome
print (nome_completo)

# * operador que repete a string int vezes
padrao = 'bip'
padrao_repetido = padrao * 5
print(padrao_repetido)