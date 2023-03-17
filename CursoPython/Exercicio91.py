# Crie um programa onde 4 jogadores joguem um dado e tenha resultados eleatórios. Guarde esses resultados em um
#dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from operator import itemgetter # para colocar um dicionario em ordem
from random import randint
from time import sleep
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3':  randint(1, 6),
        'jogador4':  randint(1, 6)}
print('Valores sorteados:')
ranking = []
for k, v in jogo.items():
    print(f'{k} tirou no dado {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # para colocar um dicionário em ordem
print('  ======Ranking dos Jogadores======  ')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)
print('  ====FIM DO JOGO====  ')