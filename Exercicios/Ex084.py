temp = []
prin = []
mai = men = 0
while True:
    temp.append(str(input('Digite o nome: ')))
    temp.append(float(input('Digite o peso: ')))
    if len(prin) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    prin.append(temp[:])
    temp.clear()
    cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont not in 'SN':
        print('Você digitou errado amigo!')
        cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'Obtivemos um total de {len(prin)} pessoas cadastradas!')
print(f'O maior peso foi de {mai}Kg. peso de ', end='')
for p in prin:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in prin:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
        
#Programa no qual apresentamos uma lista composta, para apresentar dados como quem teve o maior e menor peso, juntamente da quantidade de pessoas cadastradas! 