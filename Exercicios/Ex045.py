from random import randint
jogo = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''Escolha sua jogada: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input("Qual sera sua jogada? "))
print("-=" * 11)
print(f"Computador jogou: {jogo[comp]}")
print(f"Jogador jogou: {jogo[jogador]}")
print("-=" * 11)
if comp == 0:
    if jogador == 0:
        print("Deu empate!")
    elif jogador == 1:
        print(f"Jogador venceu!")
    elif jogador == 2:
        print("Computador venceu!")

elif comp == 1:
    if jogador == 0:
        print("Computador venceu!")
    elif jogador ==1:
        print("Deu empate!")
    elif jogador == 2:
        print("Jogador venceu!") 

elif comp == 2:
    if jogador == 0:
        print("Jogador venceu!")
    elif jogador == 1:
        print("Computador venceu!")
    elif jogador == 2:
        print("Deu empate!")

#programa no qual recriamos a famosa brincadeira JOKENPO ou se preferir: pedra, papel ou tesoura! e com o uso de if, elif e o randint, conseguimos criar um mini jogo divertido!