casa = float(input("Qual o valor da casa? "))
sal = float(input("Qual o salario do comprador? "))
anos = int(input("Quantos anos de financiamento? "))
prest = casa / (anos * 12) 
LM = sal * 0.3
if prest < LM:
    print(f"Para pagar uma casa de R${casa} em {anos} anos, a prestação sera de R${prest}")
    print("O empréstimo pode ser CONCEDIDO!")
else:
    print(f"Para pagar uma casa de R${casa} em {anos} anos, a prestação sera de R${prest}")
    print("O empréstimo sera CANCELADO!")

#Programa no qual o usuário informa o valor da casa, o salário e a quantidade de anos do financiamento. 
# O programa calcula o valor da prestação mensal e verifica se ela não ultrapassa 30% do salário do comprador,
# decidindo se o empréstimo pode ser concedido ou não.
