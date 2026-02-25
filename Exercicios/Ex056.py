media = 0
velho = 0
mulher = 0
nom = ''
for p in range(1, 5):
    print(f"----- {p}ª PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    media += idade
    if sexo == "M" and idade > velho:
            velho = idade
            nom = nome
    if sexo == "F" and idade < 20:
            mulher += 1
print(f"A média de idade do grupo é de {media / 4} anos.")
if velho > 0:
       print(f"O homem mais velho tem {velho} e se chama {nom}.")
else:
       print("Nenhum homem foi informado!")
if mulher > 0:
       print(f"Ao todo são {mulher} mulheres com menos de 20 anos")
else:
       print("Nenhuma mulher foi informada!")

#Programa simples de analise de grupo utilizando for, acumuladores e condicionais compostas para processar dados de 4 pessoas!