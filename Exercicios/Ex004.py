a = input("Digite algo: ")
print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaços? ", a.isspace())
print("É um numero? ", a.isnumeric())
print("É alfabético? ", a.isalpha())
print("É alfanumérico? ", a.isalnum())
print("Está em maiúsculas? ", a.isupper())
print("Está em minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle())

#Programa no qual pedimos ao usuario que digite algo, e então logo em seguida retornamos uma lista contendo seu tipo primitivo e diversas outras informações!