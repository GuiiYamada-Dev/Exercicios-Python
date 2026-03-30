print("Gerador de PA")
print("-=" * 10)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 10
while cont <= 10:
    print(f"{termo} → ", end="")
    termo += razão
    cont += 1
print("PAUSA")
continuar = int(input("Quantos termos você quer mostrar a mais? "))
total += continuar
while continuar != 0:
    cont = 1
    while cont <= continuar:
        print(f"{termo} → ", end="")
        termo += razão
        cont += 1
    print("PAUSA")
    continuar = int(input("Quantos termos você quer mostrar a mais? "))
    total += continuar
print(f"Progressão finalizada com {total} termos mostrados!")

#programa de progressão aritmética, com uma nova função para que o usuario possa pedir quantas mais termos ele quiser! 



    