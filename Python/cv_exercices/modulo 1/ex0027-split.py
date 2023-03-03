# Faça um programa que leia o nome de uma pessoa e mostre em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza  primeiro = Ana  ultimo = Souza

nome = str(input('Digite seu nome: ')).strip()
nomedividido = nome.split()
primeiro_nome = nomedividido[0]
ultimo_nome = nomedividido[-1]

print('Seu primeiro nome é {}.'.format(primeiro_nome)) # (nome[0])
print('Seu último nome é {}.'.format(ultimo_nome)) # (nome[len(nome)-1])