# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados,
# Ex: Digite um numero: 1834 unidade:4 dezena:3 centena:8 milhar:1

numero = int(input('Digite um número inteiro de 0 a 9999: '))

if (len(str(numero)) == 1):
    print('Unidade:',str(numero)[0])
elif (len(str(numero)) == 2):
    print('Unidade:',str(numero)[1])
    print('Dezena:',str(numero)[0])
elif (len(str(numero)) == 3):
    print('Unidade:',str(numero)[2])
    print('Dezena:',str(numero)[1])
    print('Centena:',str(numero)[0])
elif (len(str(numero)) <= 4):
    print('Unidade:',str(numero)[3])
    print('Dezena:',str(numero)[2])
    print('Centena:',str(numero)[1])
    print('Milhar:',str(numero)[0])
else:
    print('Número inválido!')

#numero = int(input('Digite um numero inteiro de 0 a 9999: ')
#unidade = numero // 1 % 10
#dezena = numero // 10 % 10
#centena = numero // 100 % 10
#milhar = numero // 1000 % 10
#print('Analisando o numero {}...'.format(numero))
#print('Unidade: {}'.format(unidade))
#print('Dezena: {}'.format(dezena))
#print('Centena: {}'.format(centena))
#print('Milhar: {}'.format(Milhar))