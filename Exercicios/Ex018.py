from math import radians, sin, cos, tan
angulo = float(input("Digite o angulo desejado: "))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f"O angulo de {angulo} tem o SENO de {seno:.2f}, COSSENO de {cosseno:.2f} e TANGENTE de {tangente:.2f}")

#Programa no qual pedimos um angulo ao usuario, e então forncemos seu SENO, COSSENO e TANGENTE! 
#Obs: é possível usarmos apenas "import math". Nesse caso, precisaríamos chamar as funções assim:
# math.sin(), math.cos(), math.tan() e math.radians()
# Ficaria por exemplo:
# seno = math.sin(math.radians(angulo))
# Usar "from math import ..." permite chamar as funções diretamente.