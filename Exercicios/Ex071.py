print("=" * 27)
print("Banco GuiiYamada")
print("=" * 27)
valor = int(input("Qual valor você quer sacar? "))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f"Total de {totced} cédulas de R${ced}")
        totced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break

#Programa que simula o saque bancario, calculando a quantidade de cada cédula necessaria para o valor do saque determinado pelo cliente