print("-=" * 27)
print("Lojinha do Guilherme")
print("-=" * 27)
barato = ""
total = cont = menor = 0
while True:
    produto = str(input("Qual o produto? "))
    valor = float(input("Qual o valor do produto? "))
    if menor == 0:
        menor = valor
        barato = produto
    if valor < menor:
        menor = valor
        barato = produto
    total += valor
    if valor > 1000:
        cont += 1
    continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if continuar != 'S':
        break
print("-" * 10, "FIM DO PROGRAMA", "-" * 10)
print(f"O total da sua compra foi de R${total}")
print(f"Entre os produtos comprados {cont} deles é maior do que R$1000.00")
print(f"O produto mais barato foi {barato} no valor de R${menor}")

#Programa no qual criamos um pequeno sistema de estatisticas com produtos e seus valores!