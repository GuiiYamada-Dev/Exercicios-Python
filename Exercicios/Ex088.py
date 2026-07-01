import random
import time
jogadas = int(input('Quantos palpites você deseja? '))
for c in range(jogadas):
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    print(f'Jogo {c + 1}: {jogo}')
    time.sleep(1)

#Programa que gera palpites aleatorios para a MEGA SENA e os cadastra dentro de uma lista composta!