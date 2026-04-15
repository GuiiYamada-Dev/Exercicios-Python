cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input("Digite um numero entre 0 e 20: "))
    if num > 20 or num < 0:
        print("você digitou errado, tente novamente!")
    else:
       print(f"O numero digitado foi o numero: {cont[num]}")
       break
    
    #programa que escreve o numero digitado por extenso na saida, utilizando tupla