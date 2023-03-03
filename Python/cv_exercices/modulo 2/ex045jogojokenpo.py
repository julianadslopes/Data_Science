# Crie um programa que faça o computador jogar Jokenpo com você.

from random import randint # importando o modulo para sorteio da biblioteca random
from time import sleep # importando o módulo para dar pausa na biblioteca time

escolha = ('Pedra', 'Papel', 'Tesoura') # criando uma lista com as opçoes de jogada
computador = randint(1, 3) # atribuindo o sorteio da lista na variavel

print('''Escolha a sua jogada:
[1] - Pedra
[2] - Papel
[3] - Tesoura''') # mostrando na tela as opções para o jogador

jogador = int(input('Qual a sua jogada? '))
# atribuindo o valor da jogada digitada pelo usuário na variavel jogador

# condição para jogador maior que 3
if jogador > 3:
    print('Jogada inválida.')
    print('Tente outra vez...')
    exit()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)
# mostrando na tela... JO... KEN... PO

# opções do jogador
if jogador == 1:
    print('Você escolheu PEDRA')
elif jogador == 2:
    print('Você escolheu PAPEL')
elif jogador == 3:
    print('Você escolheu TESOURA')

# opções do jogador
if computador == 1:
    print('O computador escolheu PEDRA')
elif computador == 2:
    print('O computador escolheu PAPEL')
elif computador == 3:
    print('O computador escolheu TESOURA')

# para computador = 1 pedra
if computador == 1 and jogador == 1:
    print('Empate!')
elif computador == 1 and jogador == 2:
    print('Você ganhou!')
elif computador == 1 and jogador == 3:
    print('Você perdeu!')

# para computador = 2 papel
if computador == 2 and jogador == 1:
    print('Você perdeu!')
elif computador == 2 and jogador == 2:
    print('Empate!')
elif computador == 2 and jogador == 3:
    print('Você ganhou!')

# para computador == 3 tesoura
if computador == 3 and jogador == 1:
    print('Você ganhou!')
elif computador == 3 and jogador == 2:
    print('Você perdeu!')
elif computador == 3 and jogador == 3:
    print('Empate!')
