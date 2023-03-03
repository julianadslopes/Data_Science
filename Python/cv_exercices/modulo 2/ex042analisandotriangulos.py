# Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles : dois lados iguais
# Escaleno : todos os lados diferentes

reta1 = float(input('Digite o comprimento da reta 1: '))
reta2 = float(input('Digite o comprimento da reta 2: '))
reta3 = float(input('Digite o comprimento da reta 3: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 and reta1 == reta3:
        print('As três retas formam um triângulo Equilátero.!')
    elif reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('As três retas formam um triângulo Isósceles.')
    elif reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
        print('As três retas formam um triângulo Escaleno.')
else:
    print('As três retas não formam um triângulo!')

# A soma de quaisquer dos lados não pode ser menor que o terceiro lado. Se for não é formado o triângulo.