from datetime import date
ano = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - ano
print(f"O atleta tem {idade} anos!")
if idade <= 9:
    print("CLASSIFICAÇÃO: MIRIM")
elif idade <= 14:
    print("CLASSIFICAÇÃO: INFANTIL")
elif idade <= 19:
    print("CLASSIFICAÇÃO: JUNIOR")
elif idade <= 25:
    print("CLASSIFICAÇÃO: SÊNIOR")
else:
    print("CLASSIFICAÇÃO: MASTER")

#Programa no qual classificamos atletas com base em suas idades!