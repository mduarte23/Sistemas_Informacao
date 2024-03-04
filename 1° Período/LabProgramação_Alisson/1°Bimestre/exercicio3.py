
prova1= float(input('Valor da prova 1: '))
prova2= float(input('Valor da prova 2: '))
trabalho= float(input('Valor do trabalho: '))
participacao= float(input('Valor da participação: '))

PROVAS= (3*prova1)+(3*prova2)
TRABALHO= 3*trabalho
media = (PROVAS+TRABALHO+participacao)/10



print(f'O valor da média é {media}')


print ('-'*50)
sexo = input('Qual o seu sexo? (H ou M): ')
altura= float(input('Digite a sua altura em metros: '))

pesoH= (72.7*altura)-58
pesoM= (62.1*altura)-44.7

#if sexo == 'H' or sexo == 'h':
if sexo.lower () == 'h':
    print (f'O peso ideal é: {pesoH:.1f} KG')
    print ('-'*50)
else:
    print (f'O peso ideal é: {pesoM:.1f} KG')
    print ('-'*50)



