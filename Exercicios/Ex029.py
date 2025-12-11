vel = float(input("Qual foi a velocidade do veiculo ao passar pelo radar? "))
if vel > 80:
    print("\033[1;31mInfelizmente o senhor ultrapassou o maximo permitido, e tera que pagar uma multa!\033[m")
    print(f"\033[1;33mO valor da multa é de R${(vel - 80) * 7 }\033[m")
else:
    print("\033[1;32mTudo perfeito meu querido, pode passar!\033[m")

#programa no qual pedimos a velocidade do veiculo ao usuario e então retornamos com if e else caso ele não tenha ultrapassado o maximo permitido!
#e caso ele tenha ultrapassado o maximo permitido é entregue uma multa de R$7.00 para cada KM acima dos 80KM