#percorrendo uma sting
nome = "Dijkstra"

print('Forma 1')
for x in range(len(nome)):
    print (f'{x} - {nome[x]}')

print('Forma 2')

for letra in nome:
    print (letra)

print ('Forma 3')
indice = 0
while indice < len(nome):
    print (f'{indice} - {nome[indice]}')
    indice +=1