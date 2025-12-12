dist = float(input("Qual distancia sera percorrida? "))
if dist > 200:
    print(f"Como a distancia esta acima dos 200Km, você ira pagar apenas um total de R${dist * 0.45}")
else:
    print(f"Como a distancia esta entre os 200Km ou abaixo, você ira pagar um total de R${dist * 0.50}")

#programa no qual pedimos a distancia percorrida ao usuario e então retornamos o valor que sera gasto em sua viagem!
# lembrando que viagens acima de 200Km foram definidas como 0.45 cada Km e viagens de até 200Km ou abaixo 0.50!