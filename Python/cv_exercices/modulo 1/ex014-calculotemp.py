# Crie um programa que leia uma temperatura em graus °c e converta para °F

c = float(input('Digite a temperatura em °C: '))
f = (c * 9/5) + 32
print('A temperatura está em {}°C e {}°F'.format(c, f))