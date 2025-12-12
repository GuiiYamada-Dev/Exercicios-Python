n1 = float(input("Digite o primeiro segmento: "))
n2 = float(input("Digite o segundo segmento: "))
n3 = float(input("Digite o terceiro segmento: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Podem formar um TRIANGULO")
else:
    print("Não podem formar um TRIANGULO")

#Programa no qual pedimos ao usuario 3 segmentos e então informamos se eles podem ou não formar um TRIANGULO!