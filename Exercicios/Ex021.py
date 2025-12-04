import pygame 
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("ex021song.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)


# Programa que toca uma música usando a biblioteca pygame.
# Inicializamos o pygame e o mixer de áudio, carregamos o arquivo MP3 e mantemos o programa rodando até a música terminar de tocar.