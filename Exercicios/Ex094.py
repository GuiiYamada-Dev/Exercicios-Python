pessoas = dict()
total = list()
mulheres = list()
mediap = list()
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo: [M/F]: ')).strip().upper()
    pessoas['Idade'] = int(input('Idade: '))
    if pessoas['Sexo'] == 'F':
        mulheres.append(pessoas.copy())
    total.append(pessoas.copy())
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar in 'N':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(total)} pessoas.')
soma = 0
for p in total:
    soma += p['Idade']
media = soma / len(total)
print(f'A media do grupo cadastrado foi {media} anos.')
print('As Mulheres cadastradas foram: ', end='')
for w in mulheres:    
    print(w['Nome'], end=' ')
for m in total:
    if m['Idade'] > media:
        mediap.append(m.copy())
print()
for pessoas in mediap:
    print(f'Nome = {pessoas['Nome']}; Sexo = {pessoas['Sexo']}; Idade = {pessoas['Idade']};')

#Programa no qual o usuario fornece informações de varias pessoas, e no final os dados são mostrados separadamente, como quantidade de pessoas, media de idade, lista de mulheres e lista das pessoas com a idade acima da media do grupo informado!