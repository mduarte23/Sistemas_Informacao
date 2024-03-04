# 2-Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome= input('Digite o seu nome: ')
senha= input('Digite sua senha: ')

while nome == senha:
    nome= input('Sua senha não pode ser igual o seu nome, digite o nome novamente: ')
    senha= input('Digite uma senha diferente do nome: ')
print (f'{nome}, sua senha é {senha}')