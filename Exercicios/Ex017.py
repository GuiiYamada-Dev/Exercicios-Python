from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print(f"A hipotenusa vai medir {hi:.2f}")

#Programa no qual pedimos ao usuario os valores do comprimento do cateto oposto e adjacente, e então retornamos o comprimento da hipotenusa.