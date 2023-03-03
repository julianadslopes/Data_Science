#Faça um programa que leia a altura e a largura de uma parede em metros
#Calcule a sua area e a quantidade de tinta para pinta-la
#Considere que cada litro de tinta pinta uma area de 2m quadrados

alt = float(input('Digite a altura da parede em metros: '))
larg = float(input('Digite a largura da parede em metros: '))
area = alt*larg
tinta = area/2
print('Sua parede tem uma dimensao de {}m x {}m com uma area de {:.3}m²'.format(alt, larg, area))
print('Quantidade de tinta necessaria: {:.3} litros'.format(tinta))
