# Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual sera a base da conversão.
# 1 para binário, 2 para octal, 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O numero {} tem o valor binário de {}.'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O numero {} tem o valor octal de {}.'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O numero {} tem o valor hexadecimal de {}.'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida.')
