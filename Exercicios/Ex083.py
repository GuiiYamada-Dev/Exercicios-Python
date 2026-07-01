expressão = input('Digite uma expressão: ')
pilha = []

for simbolo in expressão:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            print('Expressão invalida, expressão fechada sem abertura.')
            break
else:
    if len(pilha) == 0:
        print('Expressão valida')
    else:
        print('Expressão invalida, Expressão aberta sem fechamento.')

#Programa no qual validamos expressões basicas!