from time import sleep
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
escolha = 0
while escolha != 5:    
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")
    escolha = int(input("Qual das tarefas acima deseja que o programa realize? "))
    if escolha == 1:
        print(f"A soma entre os valores {n1} e {n2} é equivalente a {n1 + n2}")
    elif escolha == 2:
        print(f"A multiplicação entre os valores {n1} e {n2} é equivalente a {n1 * n2}")
    elif escolha == 3:
        if n1 > n2:
            print(f"Entre os valores {n1} e {n2} o maior valor digitado foi {n1}")
        elif n1 == n2:
            print(f"Os valores são iguais! por tanto o maior reside em ambas as posições, sendo ele o numero {n1}")
        else: 
            print(f"Entre os valores {n1} e {n2} o maior valor digitado foi {n2}")
    elif escolha == 4:
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))
    elif escolha == 5:
        print(f"Obrigado por utilizar nosso programa!")
    else:
        print("Ops! Parece que você digitou errado, tente novamente!")
    print("=-=" * 20)
    sleep(1)

#programa no qual criamos um menu de opções para que o usuario possa decidir o que fazer com os dois primeiros numeros digitados!


