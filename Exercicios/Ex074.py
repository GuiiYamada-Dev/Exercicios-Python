from random import randint
num = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100))
for n in num:
    print(n, end=" ")
print(f"\nO maior numero foi {max(num)}, e o menor numero foi {min(num)}")

#programa n o qual criamos uma tupla com numeros sorteados e então dizemos qual foi o maior e menor valor dentro dela!