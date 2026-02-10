termo = int (input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = termo + (10 - 1) * razão
for c in range (termo, décimo, razão):
    print(f"{c} ", end= '⭢ ')
print("ACABOU")

#Programa no qual temos o primeiro termo e a razão de uma PA e então mostramos os 10 primeiros termos dessa progressão.