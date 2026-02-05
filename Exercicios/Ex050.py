soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f"Digite o {c}º numero: "))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f"Foram informados {cont} numeros PARES e a soma deles foi {soma}")

#programa no qual é lido 6 numeros e feita a soma apenas dos numeros PARES digitados!
