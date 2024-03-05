#10 Faça um algoritmo que receba “N” números e mostre positivo, negativo ou zero para cada número

qtd = int(input('Informe a quantidade de números que deseja verificar: '))
contador = 0

while contador < qtd:
    numero= float(input('Digite o número que deseja verificar: '))
    contador+=1
    if numero < 0:
        print (f'{numero} é negativo.')
    elif numero > 0:
        print (f'{numero} é positivo.')
    else:
        print(f'{numero} é zero.')
    
