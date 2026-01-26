soma = 0
total = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        total += 1
print(f'A soma de todos os valores solicitados é {soma} e foram somados {total} numeros.')

#Programa no qual utilizando for, somamos apenas os valores impares que são divisiveis por 3! 