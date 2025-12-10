frase = str(input("Digite uma frase: ")).upper().strip()
print(f"A letra A aparece {frase.count('A')} vezes na frase!")
print(f"A primeira letra A apareceu na posição {frase.find('A')+1}")
print(f"A ultima letra A apareceu na posição {frase.rfind('A')+1}")

#Programa no qual pedimos ao usuario que digite uma frase e então informamos a quantidade de letras A em sua frase, juntamente da primeira e ultima posição da letra!