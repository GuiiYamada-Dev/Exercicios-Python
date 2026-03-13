sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]
while sexo not in ['M', 'F']:
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo corretamente: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")

#Programa que validade apenas a entrada dos caracteres corretos, sendo eles 'mM' ou 'fF'