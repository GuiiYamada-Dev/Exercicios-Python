sal = float(input("Qual o salario do funcionario? R$"))
if sal <= 1250:
    aum = sal + (sal * 15/100)
    porc = 15
else:
    aum = sal + (sal * 10/100)
    porc = 10
print(f"Parabens! você recebeu um aumento de {porc}%! e seu salario que antes era de R${sal:.2f} agora sera de R${aum:.2f}")


#programa no qual pegamos o valor do pagamento de um funcionario e lhe damos um aumento com base no seu salario atual sendo ou não maior que R$1250!