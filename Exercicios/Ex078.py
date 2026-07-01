valores = []
MAIOR = ''
MENOR = ''
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-' * 30)
print(f'Você digitou os valores: {valores}')
maior = max(valores)
menor = min(valores)
for c, v in enumerate(valores):
    if v == maior:
        MAIOR += f'{c}...'
    if v == menor:
        MENOR += f'{c}...'
print(f'O maior valor digitado foi {maior} nas posições {MAIOR}')
print(f'O menor valor digitado foi {menor} nas posições {MENOR}')

#Programa que usando lista, após uma leva de numeros digitado pelo usuario, retorna qual foi o maior e menor, juntamente de em qual posições eles se encontram!