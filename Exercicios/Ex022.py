nome = str(input("Digite seu nome completo: ")).strip()
separa = nome.split()
print("Ao observar seu nome...")
print(f"Seu nome em maiusculas é {nome.upper()}.")
print(f"Seu nome em minusculas é {nome.lower()}.")
print(f"Seu nome tem um total de {len(nome) - nome.count(" ")} letras.")
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras")


#Programa no qual analisamos um nome completo e o entregamos utilizando maisculas e minusculas, juntamente da quantidade de letras!