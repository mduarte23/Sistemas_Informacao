""" Faça um programa para gerar a citaçao a partir de um nome 
Ex: Carolina Maria de Jesus - JESUS, C. M. de
Gerar tambem um login = carolina.jesus"""

nome_completo = 'Carolina Maria de Jesus'
#retirar os espaços no inicio e no fim da string
nome_completo = nome_completo.strip()
#separar a string pelo espaço
partes = nome_completo.split(' ')
print (partes)
login = partes[0].lower() + "." + partes[-1].lower()
print (login)

sobrenome = partes[-1]
citacao = sobrenome.upper() + ", "
print (citacao)

for indice in range (len(partes) -1):
    parte = partes[indice]
    if parte != 'de' and parte != 'dos':
        citacao = citacao + parte[0] + ". "
    else:
       citacao = citacao + parte + ". "
print (citacao)