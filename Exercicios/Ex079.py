numeros = []
while True:
    num = int(input('Digite um numero: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Numero repetido! Não vou adicionar...')

    cont = input('Deseja continuar[S/N]: ').strip().upper()[0]
    if cont == 'N':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')

#Programa no qual utilizando Listas, permitimos ao usuario a digitação apenas de numeros que não foram digitados anteriormente!