#8- Faça um algoritmo que receba a idade de 75 pessoas e mostre mensagem informando “maior de idade” e “menor de idade” para cada pessoa. Considere a idade a partir de 18 anos como maior de idade.



for x in range (75):
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        print('É maior de idade.')
    else: 
        print('É menor de idade.')