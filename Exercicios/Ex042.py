n1 = int(input("Primeiro segmento: "))
n2 = int(input("Segundo segmento: "))
n3 = int(input("Terceiro segmento: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Os segmentos PODEM FORMAR um triângulo ", end='')
    if n1 == n2 == n3:
        print("EQUILÁTERO!")
    elif n1 != n2 != n3 != n1:
        print('ESCALENO!')
    else:
        print("ISÓSCELES")        
else:
    print("Não podem formar um triangulo ")


#programa no qual melhoramos o exercicio 35, adicionando nesse os tipos de triangulo que podem ser formados!
