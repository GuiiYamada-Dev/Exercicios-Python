numeros = []
impares = []
pares = []
while True:
    num = int(input('Digite um numero: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    cont = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while cont not in 'SN':
        print('Digitou errado amigo.')
        cont = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if cont in 'N':
        break

print(f'Os numeros digitados foram {numeros}')
if pares:
    print(f'Os numeros pares digitados foram: {pares}')
else:
    print('Não existem numeros pares dentre os valores digitados')

if impares:
    print(f'Os numeros impares digitados foram: {impares}')
else:
    print('Não existem numeros impares dentro os valores digitados')

#Programa no qual trabalhamos com mais de uma lista para separar os numeros digitados pelo usuario em uma lista de impares e pares!