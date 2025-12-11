from random import randint
print("Vou pensar em um numero entre 0 e 5.")
pc = randint(0, 5)
jogador = int(input("Em qual numero acha que eu pensei? "))
if jogador == pc:
    print(f"Parabens, vc acertou! eu realmente pensei no numero {pc}")
else:
    print(f"Que pena, vc errou! eu pensei no numero {pc}")

#programa no qual sorteamos um numero usando o randint, e então o usuario tenta acertar o numero sorteado pelo radint! 