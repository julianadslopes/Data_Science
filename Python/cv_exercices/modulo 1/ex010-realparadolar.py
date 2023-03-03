#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Considere US$ 1.00 = R$ 5.17

real = float(input('Quantos reais voce tem na carteira? '))
dolar = real / 5.17
print('Com {} reais voce pode comprar {} dolares'.format(real, dolar))