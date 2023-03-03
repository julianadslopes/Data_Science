# Crie um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele

x = input('Digite algo: ')

print('O tipo primitivo é:', type(x))
print('É numerico:', x.isnumeric())
print('É alfabetico:', x.isalpha())
print('É decimal:', x.isdecimal())
print('É minusculo:', x.islower())
print('É maiusculo:', x.isupper())
print('É impresso:', x.isprintable())
print('É alfanumerico:', x.isalnum())
print('É somente espaço: ', x.isspace())
print('É capitalizado: ', x.istitle())