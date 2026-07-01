num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º numero: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'os valores pares foram {num[0]} ')
print(f'os valores impares foram {num[1]}')

#Programa no qual utilizamos uma lista unica porem mantendo separados os valores pares e impares!