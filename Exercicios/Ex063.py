print("=" * 15)
print("Sequencia de Fibonacci")
print("=" * 15)
mostrar = int(input("Quantos termos você quer mostrar? "))
print("~" * 15)
cont = 1
n1 = 0
n2 = 1
while cont <= mostrar:
    print(f"{n1} → ", end="")
    n3 = n1
    n1 = n2
    n2 = n3 + n1
    cont += 1
print("FIM")

#Programa no qual faz uma sequencia de fibonacci com a quantidade de termos selecionada pelo usuario!
    