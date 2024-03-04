import requests
import random

url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'

response = requests.get(url)
print (response.text)
palavras = response.text.split('\n') #separa por blocos sendo casa posiçao uma palavra
n_palavras = (len(palavras)) #qtde de palavras
posicao_sorteada = random.randint(0,n_palavras).upper()

secreta1 = random.choice(palavras).upper() #choice sorteia uma palavras upper deixa a palavra maisucula