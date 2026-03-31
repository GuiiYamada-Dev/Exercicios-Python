print("-=" * 15)
print("Cadastro de pessoas")
print("-=" * 15)
pessoas = homens = mulheres = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = str(input("Qual o sexo? [M/F]: ")).strip().upper()
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres +=1
    if idade > 18:
        pessoas += 1
    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if continuar != 'S':
        break
if pessoas == 0:
    print("Nenhuma das pessoas cadastradas é maior de 18 anos!")
else:
    print(f"Ao todo {pessoas} pessoas cadastradas tem mais do que 18 anos!")
if homens == 0:
    print("Não foi encontrado nenhum homem cadastrado!")
else:
    print(f"Ao todo foram cadastrados {homens} homens!")
if mulheres == 0:
    print("Nenhuma mulher com menos de 20 anos cadastrada!")
else:
    print(f"Ao todo foram cadastradas {mulheres} mulheres com menos de 20 anos! ")

#Programa de cadastro de pessoas com filtros de idade e sexo!
