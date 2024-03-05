#7- Ler 80 números e ao final informar quantos número(s) est(á)ão no intervalo entre 10 (inclusive) e 150 (inclusive)
contador = 0
for x in range (80):
    numero = int(input('Digite o número: '))
    if numero >= 10 and numero <= 150:
        contador +=1
print(f'{contador} números estão no intervalo entre 10 e 150.')
