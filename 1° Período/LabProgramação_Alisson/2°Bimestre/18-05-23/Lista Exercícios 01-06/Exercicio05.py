# 5- Faça um programa que calcule e mostre a média aritmética de N notas. N equivale ao total de avaliaçoes.

qtd= int(input('Digite a quantidade de notas que será feito a média: '))
total = 0
contador = 1

while contador <= qtd:
    avaliacao = float(input(f'Digite o valor da prova {contador}: '))
    contador +=1
    total = avaliacao + total

media = total/qtd

print (f'A média das {qtd} provas foi de {media}')

