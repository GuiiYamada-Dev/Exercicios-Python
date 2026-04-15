times = ('Palmeiras', 'Flamengo', 'São Paulo', 'Fluminense', 'Bahia', 'Athletico-PR', 'Coritiba', 'Atlético-MG', 'Bragantino', 'Vitoria', 'Botafogo', 'Gremio', 'Vasco', 'Internacional', 'Santos', 'Corinthians', 'Cruzeiro', 'Remo', 'Chapecoense', 'Mirassol')

print("os cinco primeiros colocados da tabela são:")
print(" ".join(times[:5]))
print("=-" * 15)

print("Os 4 ultimos colocados da tabela são:")
print(" ".join(times[-4:]))
print("=-" * 15)

print("Os 20 colocados da tabela em ordem alfabetica: ")
ordem = sorted(times)
print(" ".join(ordem))
print("=-" * 15)

print(f"O time da Chapecoense esta na posição {times.index('Chapecoense')+1}º")


#Programa testando algumas das funcionalidades das tuplas














