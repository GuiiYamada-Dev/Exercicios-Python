n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f"O maior numero digitado foi {maior}")
print(f"O menor numero digitado foi {menor}")

#programa no qual pedimos ao usuario para digitar três numeros e então mostramos na tela qual foi o maior e qual foi o menor dos digitados!