from datetime import date
ano = int(input("Ano de nascimento: "))
atual = date.today().year
idade = atual - ano
print(f"Você nasceu no ano de {ano}, então você ja esta com {idade} anos no ano atual de {atual}")
if idade > 18:
    print(f"Ih rapaz você ja deveria ter se alistado... seu alistamento foi a {idade - 18} anos atras, no ano de {atual - (idade - 18)}")
if idade < 18:
    print(f"Opa, ainda não chegou sua hora de se alistar! você ira se alistar daqui {18 - idade} anos, no ano de {atual + (18 - idade)}")
if idade == 18:
    print(f"Tempo perfeito! seu ano de alistamento é esse mesmo!")

#Programa no qual pegamos a data de nascimento do usuario e verificamos a questão do alistamento!
#para então sabermos se ele ainda não deve se alistar, se ele ja pode se alistar ou se ele ja perdeu a data do alistamento.