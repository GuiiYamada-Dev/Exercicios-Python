n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
n3 = int(input("Digite mais um numero: "))
n4 = int(input("Digite o ultimo numero: "))
Ns = (n1, n2, n3, n4)
nove = 0
print(f"Os valores digitados foram: {Ns}")
print(f"Os valores pares digitados foram: ",end='')
for c in Ns:
    if c % 2 == 0:
        print(c, end=' ')
    if c == 9:
        nove += 1
if nove > 0:
    print(f"\nO numero 9 apareceu {nove} vezes")
else:
    print("O numero 9 não foi digitado!")
if 3 in Ns:
    print(f"O numero 3 foi digitado pela primeira vez na posição {Ns.index(3)+1}")
else:
    print("O numero 3 não foi digitado")

#programa no qual damos a liberdade do usuario escrever os numeros que são inseridos dentro da tupla e então mostramos algumas informações! 

