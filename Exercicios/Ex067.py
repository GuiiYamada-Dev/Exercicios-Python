while True:
    tab = int(input("Quer ver a tabuada de qual valor? "))
    if tab <= 0:
        break
    print("-=" * 15)
    for c in range(1, 11):
        print(f"{tab} X {c} = {tab * c}")
    print("-=" * 15)
print("Programa encerrado, volte sempre!")

#Programa no qual pedimos um numero ao usuario e então entregamos a tabuada do numero, o encerramento da tabuada ocorre quando 0 ou um valor negativo é digitado!