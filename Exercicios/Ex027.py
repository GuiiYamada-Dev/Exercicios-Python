n = str(input("Digite seu nome completo: ")).strip()
nome = n.split()
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu ultimo nome é {nome[len(nome)-1]}")

#Programa no qual pedimos ao usuario para digitar seu nome completo e em seguida com a ajuda do split, retornamos qual é o primeiro e qual é o ultimo nome!