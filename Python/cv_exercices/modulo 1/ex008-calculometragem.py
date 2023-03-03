#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
#Converta também para quilometros, hectometros, decametros e decimetros

valorm = float(input('Digite um valor em metros: '))
cm = valorm * 100
mm = valorm * 1000
dam = valorm * 10
dec = valorm / 10
km = valorm / 1000
hc = valorm / 10000
print('{}m é igual a {:.0f}cm'.format(valorm, cm))
print('{}m é igual a {:.0f}mm'.format(valorm, mm))
print('{}m é igual a {:.0f}dam'.format(valorm, dam))
print('{}m é igual a {:.0f}dec'.format(valorm, dec))
print('{}m é igual a {}km'.format(valorm, km))
print('{}m é igual a {}hc'.format(valorm, hc))