from random import shuffle
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
apresentação = [n1, n2, n3, n4]
shuffle(apresentação)
print(f"A ordem de apresentação sera:")
print(apresentação)

#Programa no qual pedimos novamente 4 nomes ao usuario e então ao utilizar o shuffle da biblioteca random, nós entregamos a apresentação que antes estava em uma ordem agora de forma sorteada!