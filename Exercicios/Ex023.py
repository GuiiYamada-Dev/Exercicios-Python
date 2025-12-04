num = int(input("Digite um numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Ao analisar o numero digitado {num}")
print("Nós temos:")
print(f"Sua Unidade {u}")
print(f"Sua Dezena {d}")
print(f"Sua Centena {c}")
print(f"Seu Milhar {m}")

#Programa no qual pedimos um numero ao usuario e informamos sua unidade, dezena, centena e milhar!