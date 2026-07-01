aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Qual foi a media de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Media'] <= 5:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Recuperação'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
    
#Programa no qual usando Dicionarios, lemos o nome e média de um aluno guardando tb sua situação e então a entregando no final!