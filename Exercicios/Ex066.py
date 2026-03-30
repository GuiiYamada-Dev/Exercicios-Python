soma = cont = 0
while True:
    n1 = int(input("Digite um valor [999 para parar]: "))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f"A soma dos {cont} valores foi {soma}")

#Programa que soma números digitados até o usuário digitar 999 (tal qual ex 64, porem agora utilizando while True e break)