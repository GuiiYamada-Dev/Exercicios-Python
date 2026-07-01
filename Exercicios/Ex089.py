ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while cont not in 'SN':
        print('Digitou errado')
        cont = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f"{'No.':<4}{'NOME':<15}{'Média':>6}")
print('-' * 40)
for indice, valor in enumerate(ficha):
    print(f"{indice:<4}{valor[0]:<15}{valor[2]:>6.1f}")
while True:
    nota = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if nota < len(ficha):
        print(f'Notas de {ficha[nota][0]}: {ficha[nota][1]}')
    if nota == 999:
        break

#Programa no qual é lido duas notas de varios alunos, guardado em uma lista composta, e no final é mostrado um boletim contendo a média de cada um permite ao usuario ver individualmente a nota de cada um!  



