n1 = int(input("Digite um numero: "))
soma = maior = menor = n1
cont = 1
continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()
while continuar == "S":
    n1 = int(input("Digite um numero: "))
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
    soma += n1
    cont += 1
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
print(f"Você digitou {cont} numeros e a media deles foi {soma / cont}")
print(f"O maior valor foi {maior} e o menor valor foi {menor}")

#Programa no qual o usuario informa numeros até achar que foi o bastante, e no final mostramos na tela quantos foram digitados, a media da soma entre eles, e quais foram os maiores e menores!

        