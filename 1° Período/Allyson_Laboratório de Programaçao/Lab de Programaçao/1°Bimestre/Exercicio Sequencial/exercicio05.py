# exercicio 05

valor = int(input('Digite o valor em centavos: '))
moedas1real = valor // 100 #devolve a parte inteira da divisão
resto= valor%100 #% calcula o resto da divisão
moedas50cents = resto // 50
resto = resto%50
moedas25cents = resto // 25
resto = resto % 25
moedas10cents = resto //10
resto = resto % 10
moedas5cents = resto // 5
moedas1cents = resto% 5

print (f'Para o valor de {valor} centavos sera necessário:')
print (f'{moedas1real} moedas de R$1,00')
print (f'{moedas50cents} moedas de R$0,50')
print (f'{moedas25cents} moedas de R$0,25')
print (f'{moedas10cents} moedas de R$0,10')
print (f'{moedas5cents} moedas de R$0,05')
print (f'{moedas1cents} moedas de R$0,01')
