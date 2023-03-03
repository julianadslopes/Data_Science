# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porçao inteira.
# Ex: digite um numero 6.127. O numero 6.127 tem a parte inteira 6.

from math import trunc

n = float(input('Digite um numero real: '))
ni = trunc(n)
print('O numero {} tem sua parte inteira {}'.format(n, ni))