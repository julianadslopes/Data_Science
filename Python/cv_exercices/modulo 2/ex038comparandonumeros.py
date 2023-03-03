# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

numero1 = int(input('Digite o primeiro numero: '))
numero2 = int(input('Digite o segundo numero: '))

if numero1 > numero2:
    print('O número {} é maior que o número {}.'.format(numero1, numero2))
elif numero1 < numero2:
    print('O número {} é menor que o número {}.'.format(numero1, numero2))
else:
    print('Os dois números são iguais!')
