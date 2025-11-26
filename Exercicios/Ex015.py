dias = int(input("Por quantos dias você ira alugar o carro? "))
print("~" * 30)
print("Após a o tempo passar")
print("~" * 30)
km = float(input("Opa! espero que tenha ocorrido tudo certo! quantos KM você percorreu com o veiculo? "))
valor = (dias * 60) + (km * 0.15)
print("~" * 30)
print(f"Perfeitamente! tendo alugado o carro conosco por {dias} dias e rodado {km} Km, o valor a pagar sera de R${valor}")

#Programa no qual calculamos o valor de um aluguel de carro, sendo que a diria equivale a R$60 e cada KM equivale a R$0,15