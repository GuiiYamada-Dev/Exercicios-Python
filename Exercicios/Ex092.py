dados = dict()
from datetime import date
nome = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
ctps = int(input('Carteira de trabalho: (0 não tem) '))
hoje = date.today().year
idade = hoje - nascimento
dados['Nome'] = nome
dados['Idade'] = idade
dados['ctps'] = ctps 
if ctps != 0:
    cont = int(input('Ano de contrato: '))
    sal = float(input('Salario: '))
    aposen = cont + 35
    idApo = aposen - nascimento
    dados['Contratação'] = cont
    dados['Salario'] = sal
    dados['Aposentadoria'] = idApo
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}')

#Programa que cadastra nome, idade e CTPS de uma pessoa; se tiver carteira assinada, calcula ano de aposentadoria (contratação + 35 anos)