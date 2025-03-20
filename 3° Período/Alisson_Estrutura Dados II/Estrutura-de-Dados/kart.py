import random

def soma(x):
    soma = sum(x)
    return soma

def melhor_tempo(x):
    tempo = x[0]
    posicao = 0
    for i in range(len(x)):
        if tempo >  x[i]:
            tempo = x[i]
            posicao = i
    return posicao

def media (l):
    lista_soma=[]    
    for x in range(len(l)):
        total = []
        for y in range (len(l)):
            total.append(l[y][x])           
        media = sum(total) / len(l)
        lista_soma.append(media)
    return lista_soma

    


matriz = []
corredores = ["Piloto 1","Piloto 2","Piloto 3", "Piloto 4", "Piloto 5","Piloto 6"]
n_voltas = ["Volta 1", "Volta 2", "Volta 3", "Volta 4", "Volta 5", "Volta 6", "Volta 7","Volta 8","Volta 9", "Volta 10"]
for x in range(len(corredores)):
    volta = []
    for y in range(len(n_voltas)):
        aleatorio = random.randint(90,120)
        volta.append(aleatorio)
    matriz.append(volta)

print('Tabela de Voltas')
print()
print ("\t", end= "\t")
contador = 1
for i in range(len(n_voltas)):
    print(n_voltas[i], end= "\t")
    contador += 1
print()

for l in range(len(corredores)):
    print (corredores[l], end = "\t")
    for m in range(len(n_voltas)):
        print (matriz[l][m], end = "\t")
    print()

print()
print ("_"*50)
print ("a) De quem foi a melhor volta da prova, e em que volta")

menor = matriz[0][0]
piloto = []
melhor_volta = []

for linha in range(len(corredores)):
    for coluna in range(len(n_voltas)):
        if menor > matriz[linha][coluna]:
            piloto = []
            melhor_volta = []
            menor = matriz[linha][coluna]
            piloto.append(corredores[linha])
            melhor_volta.append(n_voltas[coluna]) 
        elif menor == matriz[linha][coluna]:
            piloto.append(corredores[linha])
            melhor_volta.append(n_voltas[coluna]) 
if len(piloto) > 1:
    for x in range(len(piloto)):
        print(f"{piloto[x]}, {melhor_volta[x]}", end="\t")
    print()
else:
    print(f"{piloto[0]}, {melhor_volta[0]}")

print()
print ("_"*50)
print("b) Classificação final em ordem (1º o campeão)")
t_voltas = []
for i in range(len(corredores)):
    total = soma(matriz[i])
    t_voltas.append(total)

classificacao = []
tempo_total = []
while len(t_voltas) > 0:
    posicao = melhor_tempo(t_voltas)
    classificacao.append(corredores[posicao])
    tempo_total.append(t_voltas[posicao])
    t_voltas.remove(t_voltas[posicao])
    corredores.remove(corredores[posicao])

print ("", end="\t")
print("Classificação", end="\t")
print ("Tempo")
contador = 1
for i in range (len(classificacao)):
    print (f"{contador}°", end="\t")
    print (classificacao[i], end="\t")
    print (tempo_total[i])
    contador += 1

print()
print ("_"*50)
print ("c) Qual foi a volta com a média mais rápida")

l_voltas = media(matriz)

melhor_media = melhor_tempo(l_voltas)
print (f"A volta com a média mais rápida foi {n_voltas[melhor_media]} com o tempo de {l_voltas[melhor_media]:.2f} segundos ")