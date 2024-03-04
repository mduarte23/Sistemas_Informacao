"""
Programa que gere a tabela de jogos de um campeonato que tem 5 times (times jogam em casa e na casa do adversário)
"""

times= ['COR', 'STS', 'GOI', 'CRT', 'CHA']

for time1 in times:
    for time2 in times:
        if time1 != time2:
            print (f'{time1} x {time2}')