#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5.
#Peça para que o usuário tente descobrir qual foi o numero escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from date import sleep

computador = randint(0, 5) # faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número, tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('Você venceu!')
else:
    print('Você perdeu. Eu pensei no número {} e você escolheu {}!'.format(computador, jogador))