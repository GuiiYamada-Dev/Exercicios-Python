n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
med = (n1 + n2) / 2
print(f"Tirando {n1} e {n2}, a média do aluno é {med:.1f}")
if med < 5.0:
    print("Infelizmente você foi REPROVADO!")
elif med < 6.9:
    print("Felizmente você ainda tem uma chance e esta de RECUPERAÇÃO!")
else:
    print("Parabens, você teve um otímo desempenho e esta APROVADO")

#Programa no qual calculamos a média de um aluno e então informamos se ele esta Reprovado de Recuperação ou se foi Aprovado!