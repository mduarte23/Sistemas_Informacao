"""Armazenar as notas de 3 alunos em uma lista. A nota de cada aluno será informada pelo teclado"""
qtd= int(input("Informe a quantidade de notas: "))
notas = []
valor = 1
for i in range (qtd):
    nota = float(input(f'Digite a nota {valor}: '))
    notas.append(nota)
    valor += 1
print (notas)

media = sum(notas)/len(notas) #sum = faz a soma dos números da lista
print (f'A média final é {media}')
