import random
import time
from operator import itemgetter
cont = 0
jogadores = {}
jogadores['jogador1'] = random.randint(1, 6)
jogadores['jogador2'] = random.randint(1, 6)
jogadores['jogador3'] = random.randint(1, 6)
jogadores['jogador4'] = random.randint(1, 6)
ranking = dict()
print('Valores sorteados:')
while cont < 4:
    for c, i in jogadores.items():
        print(f'O {c} tirou {i} ')
        time.sleep(1)
        cont += 1
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogares:')
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    time.sleep(1)
