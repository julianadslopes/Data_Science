# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip() # elimina os espaços antes e depois da string.
nome_dividido = nome.split()
print('Seu nome com letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome com letras minúsculas: {}'.format(nome.lower()))
print('Seu nome completo possui {} letras ao todo.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(len(nome_dividido[0])))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))