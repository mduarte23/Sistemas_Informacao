numeros = [1,4,9,16,25]
print (numeros)

numeros[1] = 6 #altera o número na posicao desejada
print (numeros)

print (numeros[-1]) #retorna o último item da lista

lista = [36, 49, 64]
nova_lista = numeros + lista #junta (une) as listas
print (nova_lista)

nova_lista.append(9*9)
print (nova_lista)
nova_lista[1] = 2**2
print (nova_lista)

#percorrer a lista exibindo apenas os valores
for valor in nova_lista:
    print (valor)

#mostrar  o indice e valor
for indice in range(len(nova_lista)):
    valor = nova_lista[indice]
    print (f'Indice = {indice}, valor = {valor}')

for indice, valor in enumerate(nova_lista): #enumerate : pega o valor do indice e do valor
    print (f'Indice = {indice}, valor = {valor}')