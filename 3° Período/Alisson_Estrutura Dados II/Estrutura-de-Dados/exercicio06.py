"""
Vamos supor que precisamos criar um programa para cadastrar alunos em uma escola, armazenando informaçoes como nome, idade e nota. Podemos utilizar um dicionário para representar cada aluno, onde a chave será o número de matricula e o valor será outro dicionário contendo as informaçoes do aluno
"""
alunos = {}
op = "S"
while op == "S":
    matricula = input('Número de matricula: ')
    while matricula in alunos:
        matricula = input('Matricula já cadastrada, tente outra: ')
    nome = input('Nome: ')
    idade = input('Idade: ')
    nota = input('Nota: ')
    alunos[matricula]= {'nome':nome, 'idade':idade, 'nota':nota}
    op = input("Deseja adicionar outro aluno? S - N: ").upper()
    while op != "S" and op != "N":
        op= input("Opção errada, digite 'S'-sim ou 'N'-não: ").upper()
print ("ALUNOS CADASTRADOS")
print (alunos)
