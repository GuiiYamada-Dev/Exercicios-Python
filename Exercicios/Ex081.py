numeros = []
while True:
    numeros.append(int(input('Digite um numero: ')))
    cont = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    while cont not in 'SN':
        print('Digitou errado')
        cont = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if cont in 'N':
        break
numeros.sort(reverse = True)
print(f'A quantidade de valores digitados foi {len(numeros)}')
print(f'Os valores digitados em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('Sim o numero 5 esta na lista')
else:
    print('O numero 5 não esta na lista')

#Programa no qual alem de deixar a lista em ordem decrescente, retiramos tb as informações de quantos numeros foram digitados, e se o numero 5 esta entre eles!