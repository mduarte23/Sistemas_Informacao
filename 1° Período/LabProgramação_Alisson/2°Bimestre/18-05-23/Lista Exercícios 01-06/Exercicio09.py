#9- Uma concessionária de veículos está vendendo os seus veículos com desconto. Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente de vários carros. O desconto deverá ser calculado de acordo com o ano do veículo. Até 2000 - 12% e acima de 2000 - 7%. O sistema deverá perguntar se deseja continuar calculando desconto até que a resposta seja: “(N) Não”. Informar total de carros com ano até 2000 e total geral.

opcao = 'S'
antigo = 0
geral = 0
while opcao == 'S':
    valor = float(input('Digite o valor do carro: '))
    ano = int(input('Digite o ano do carro com 4 digitos: '))

    if ano <= 2000:
        desconto = valor * 0.12
        pago = valor - desconto
        print (f'O carro do ano {ano} com o preço de {valor:.2f} teve desconto de R${desconto:.2f} e sairá para o cliente no valor de R${pago:.2f}') 
        antigo += 1
    else:
        desconto = valor * 0.07
        pago = valor - desconto
        print (f'O carro do ano {ano} com o preço de {valor:.2f} teve desconto de R${desconto:.2f} e sairá para o cliente no valor de R${pago:.2f}') 
    geral +=1
    opcao = input('Deseja calcular outro veículo: (S) ou (N): ')
    if opcao != 'S' and opcao != 'N':
        opcao = input('Informação inválida, digite "S" para sim ou "N" para não')
    print(f'Total de carros calculados foi {geral}, e o total de carros de ano até 2000 foi de {antigo}.')