palavras = ('guanabara', 'programando', 'concurso', 'abordagem',
            'caveira', 'caneca', 'celular', 'irmandade',
            'computador', 'refrigerante', 'virtual')
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos ', end='')
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end=' ')

#Progrma no qual colocamos varias palavras dentro de uma tupla e então mostramos as vogais de cada uma! 