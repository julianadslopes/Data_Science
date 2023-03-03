# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo.
# Calcule e mostre o comprimento da hipotenusa

from math import sqrt

coseno = float(input('Medida do cateto oposto: '))
cateto = float(input('Medida do cateto adjacente: '))
h = sqrt(coseno * coseno + cateto * cateto)
print('O valor da hipotenusa é: {:.2f}'.format(h))