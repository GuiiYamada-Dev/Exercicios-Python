itens = ("Água", 1.50,
         "Videogame", 999.99,
         "quadro", 17.98,
         "notebook", 2499.90,
         "controle", 235.70,
         "caneca", 17.50)
print('-' * 35)
print(f'{"LISTA COM OS PREÇOS":^35}')
print('-' * 35)
for c in range(0, len(itens)):
    if c % 2 == 0:
        print(f'{itens[c]:.<30}', end='')
    else:
        print(f'R${itens[c]:>7.2f}')
print('-' * 35)

#programa no qual utilizamos uma tupla unica para imprimir o nome e preço de produtos!