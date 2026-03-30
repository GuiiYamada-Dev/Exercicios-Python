n1 = cont = total = 0
n1 = int(input("Digite um numero [999 para parar]: "))
while n1 != 999:
    total += n1
    cont += 1
    n1 = int(input("Digite um numero [999 para parar]: "))
print(f"Você digitou {cont} numeros e a soma entre eles foi {total}")

#Programa no qual somamos os numeros digitados pelo usuario!