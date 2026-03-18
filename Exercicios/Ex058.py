import random
tentativas = 0
print ("Olá, sou o Guilherme, acabei de pensar em um numero entre 0 e 10 com a ajuda do computador...\nSerá que consegue adivinhar qual foi?")
numero = random.randint(0, 10)
while True:
    palpite = int(input("Qual é o seu palpite? "))
    tentativas += 1
    if palpite == numero:
        print("Mandou bem, você acertou!")
        break
    if palpite < numero:
        print("MAIOR... Tente outra vez!")
    else:
        print("MENOR... Tente outra vez!")
if tentativas > 1:
    print(f"Foram necessarias {tentativas} tentativas, para que você acertasse!")
else:
    print("Caraca, foi de primeira!")

#Programa no qual sorteamos um numero e pedimos ao usuario que tente adivinhar qual foi, somando o numero de tentativas até que ele acerte! 