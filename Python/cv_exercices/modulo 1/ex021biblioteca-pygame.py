# Faça um programa que abra e reproduza o audio de um arquivo mp3.

import pygame

pygame.init() # Inicia a biblioteca
pygame.mixer.music.load('nome do arquivo.mp3') # Lê o arquivo
pygame.mixer.music.play() # Inicia o arquivo
pygame.event.wait() # Espera o arquivo terminar para fechar o programa