peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))
imc = peso / (altura ** 2)
print(f"o IMC digitado equivale a: {imc:.1f}")
if imc < 18.5:
    print("Você esta abaixo do peso")
elif 18.5 <= imc < 25:
    print("Parabens, você esta com o peso ideal")
elif 25 <= imc < 30:
    print("Você esta com sobrepeso")
elif 30 <= imc < 40:
    print("Você esta com obesidade")
elif imc >= 40:
    print("Cuidado, você esta com Obesidade Mórbida") 

#programa no qual usamos o peso e a altura de uma pessoa e então verificamos seu imc e então entregamos o resultado sobre a massa corporal.
