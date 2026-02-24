maior = 0
menor = 0

for c in range (1, 6):
    peso = float(input(f"Peso da {c}ª pessoa: "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi de {maior}Kg")
print(f"O menor peso lido foi de {menor}Kg")

#Programa no qual utilizando for, conseguimos mostrar qual foi o maior e qual foi o menor peso digitado