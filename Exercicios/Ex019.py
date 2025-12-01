from random import choice
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
sorteio = [n1, n2, n3, n4]
escolhido = choice(sorteio)
print(f"O aluno escolhido para limpar o quadro foi: {escolhido}")

#Programa no qual o usuario fornece o nome de 4 alunos e então da biblioteca random, é utilizado o choice, para escolher dentro da lista sorteio um dos 4 alunos!