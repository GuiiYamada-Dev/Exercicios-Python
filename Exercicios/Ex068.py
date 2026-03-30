import random
print("-=" * 15)
print("Bora de PAR ou IMPAR!")
print("-=" * 15)
cont = 0
while True:
    n1 = int(input("Diga um valor: "))
    escolha = str(input("Par ou Impar? ")).strip().upper()
    pc = random.randint(0, 10)
    total = n1 + pc
    if total % 2 == 0:
      if escolha == "P":
        print(f"Você jogou {n1} e o computador jogou {pc}. O total foi {total} deu PAR!")
        print("Você venceu!")
        print("Vamos jogar novamente!")
        print("-=" * 15)
        cont += 1
      else:
        print(f"Você jogou {n1} e o computador jogou {pc}. O total foi {total} deu PAR!")
        print("Você perdeu!")
        break
    if total % 2 != 0:
        if escolha == "I":
          print(f"Você jogou {n1} e o computador jogou {pc}. o total foi {total} deu IMPAR")
          print("Você venceu!")
          print("Vamos jogar novamente!")
          print("-=" * 15)
          cont += 1
        else:
          print(f"Você jogou {n1} e o computador jogou {pc}. O total foi {total} deu IMPAR!")
          print("Você perdeu!")
          break
print(f"Game over! Você ganhou {cont} vezes! ")
        
#Programa no qual criamos um jogo de par ou impar! 