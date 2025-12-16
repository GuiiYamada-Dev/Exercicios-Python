num = int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases para conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL
[4] Converter tudo''')
opção = int(input("Sua opção: "))
if opção == 1:
    print(f"O numero inteiro {num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif opção == 2:
    print(f"O numero inteiro {num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opção == 3:
    print(f"O numero inteiro {num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
elif opção == 4:
    print(f"O numero inteiro {num} convertido para BINARIO é {bin(num)[2:]} para OCTAL é {oct(num)[2:]} e para HEXADECIMAL É {hex(num)[2:]}")
else:
    print("Opção invalida, o programa sera encerrado agora!")

#Programa no qual convertemos um numero inteiro para BINARIO, OCTAL OU HEXADECIMAL DEPENDENDO DA ESCOLHA DO USUARIO!