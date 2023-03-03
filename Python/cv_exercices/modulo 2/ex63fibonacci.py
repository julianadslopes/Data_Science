# Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

numero = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print('{} -> {}'.format(termo1, termo2), end='')
cont = 3
while cont <= numero:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont +=1
print('-> FIM')