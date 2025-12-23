print("========== LOJAS GM ==========")
valor = float(input("Qual valor total da sua compra? R$"))
print("=" * 35)
print('''FORMAS DE PAGAMENTO:
[1] a vista cédulas/pix
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
escolha = int(input("Qual sera a forma de pagamento? "))
if escolha == 1:
    pagar = valor * 0.90
    print(f"Perfeitamente! pagando a vista em dinheiro ou no pix, você recebe um desconto de 10% então ao inves de pagar R${valor:.2f}, você ira pagar apenas R${pagar:.2f}")
elif escolha == 2:
    pagar = valor * 0.95
    print(f"Perfeitamente! pagando a vista no cartão você recebe um desconto de 5% então ao inves de pagar R${valor:.2f}, você ira pagar apenas R${pagar:.2f}")
elif escolha == 3:
    print(f"Perfeitamente! parcelando sua compra de R${valor:.2f} em 2x o valor das parcelas sera de R${valor / 2:.2f}")
elif escolha == 4:
    parc = int(input("Em quantas parcelas gostaria de fazer? "))
    pagar = valor * 1.20
    print(f"Perfeitamente! parcelando sua compra de R${valor:.2f} devido aos juros ela ficara no valor de R${pagar:.2f}")
    print(f"Como você decidiu parcelar a sua compra em {parc}x o valor de cada parcela sera de R${pagar / parc:.2f}")

#programa no qual pedimos o valor da compra ao usuario e então fornecemos formas de pagamento cada uma com seus descontos e juros! 


