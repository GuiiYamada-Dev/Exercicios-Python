from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(7):
    pessoa = int(input(f"Em que ano a {c + 1}ª pessoa nasceu? "))
    idade = atual - pessoa
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade!")
print(f"E também tivemos {menor} pessoas menores de idade!")

#Programa no qual conta o numero de pessoas maiores e menores, utilizando a simplicidade do for!