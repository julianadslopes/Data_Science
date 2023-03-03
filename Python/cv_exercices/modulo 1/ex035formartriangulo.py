#Desenvolva um programa que leia o comprimento de 3 restas.
#Diga ao usuário se elas podem ou não formar um triangulo.

reta1 = float(input('Digite o comprimento da reta 1: '))
reta2 = float(input('Digite o comprimento da reta 2: '))
reta3 = float(input('Digite o comprimento da reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('As três retas formam um triângulo!')
else:
    print('As três retas não formam um triângulo!')