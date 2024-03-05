"""Crie duas lista em python, uma para armazenar o nome e outra lista para armazenar a idade.
Posteriormente indique quais pessoas tem 18 anos ou mais e quantas pessoas são menores de idade.
Ex.:
Joese , 10 anos
Joaquim, 19 anos
Jailton, 30 anos
Juarez, 5 anos
João, 18 anos
--> São maiores de idade: Joaquim, Jailton, Joao
--> São menores de idade: Jose, Juarez"""

nomes = []
idade = []
maior = "São maiores de idade: "
menor = "São menores de idade: "
quantidade = 5
for x in range(quantidade):
    tmp = input(f'Digite o {x+1}° nome:')
    nomes.append(tmp)
    idade.append(int(input(f'Digite a idade de {tmp}: ')))

for y in range(len(idade)):
    if idade[y] >= 18:
        tmp = nomes[y]
        maior = maior + tmp + ', '
    else:
        tmp = nomes[y]
        menor = menor + tmp + ', '
print(maior[:-2])
print(menor[:-2])