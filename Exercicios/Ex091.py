import random
from operator import itemgetter
jogadas = dict()
for c in range(0, 4):
    dado = random.randint(1, 6)
    print(f'O jogador {c + 1} tirou {dado}')
    jogadas[f'Jogador {c + 1}'] = dado
ranking = list()
ranking = sorted(jogadas.items(), key = itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar ficou o {v[0]} com {v[1]} pontos no dado.')

#Programa no qual usando os dicionarios, geramos 4 numeros aleatorios para cada um dos jogadores, e então os colocamos em ordem do maior ao menor ponto!