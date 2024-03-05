notas = [8, 5.5, 1.5]
#print (notas[3]) #Indice inválido, precisa se 0, 1 ou 2
#tam = len(notas) # len -> length - comprimento da ED
#print (tam) 
media = (notas[0] + notas [1] + notas[2]) / 3
print (f'Média = {media:.2f}')

media2 = (notas[0] + notas [1] + notas[2]) / len(notas)
print (f'Média = {media2:.2f}')

notas3 = [8, 5.5, 1.5, 9]
media3 = (notas3[0] + notas3[1]+ notas3[2] + notas3[3])/ len(notas3)
print (f'Média = {media3:.2f}')

print ('----------FOR---------------')
notas3 = [8, 5.5, 1.5, 9, 10]
soma = 0
for indice in range (len(notas3)):
    #print (indice, end='>>>>')
    #print (notas3[indice])
    soma = soma + (notas3[indice])
   
media3 = soma / len(notas3)

print (f'Média = {media3:.2f}')

