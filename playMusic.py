
import pygame

pygame.init()
pygame.mixer.init()

# Carrega e toca o áudio
pygame.mixer.music.load('HINO DO CORINTHIANS.mp3')  # Use .mp3 ou .wav
pygame.mixer.music.play()

# Espera o áudio terminar
while pygame.mixer.music.get_busy():
    continue

print("Áudio terminou!")