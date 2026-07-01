jogo = dict()
total = list()
soma = 0
nome = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {nome} jogou? '))
for c in range(partidas):
    gols = int(input(f'Quantos gols {nome} marcou na partida {c + 1}? '))
    total.append(gols)
    soma += gols
jogo['Nome'] = nome
jogo['gols'] = total
jogo['Total'] = soma
print('-=' * 30)
print(jogo)
print('-=' * 30)
for k, v in jogo.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'o jogador {nome} jogou {partidas} partidas.')
for p, q in enumerate(total):
    print(f'=> Na partida {p + 1}, o jogador {nome}, fez {q} gols.')
print(f'Foi um total de {soma} gols')

#Programa no qual o usuario digita os dados sobre um jogador e em seguida é mostrado na tela o aproveitamento desse jogador!