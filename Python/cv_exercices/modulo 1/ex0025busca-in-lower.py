# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite o nome de uma pessoa: ')).strip()
print('A pessoa informada tem Silva no nome? '.format('silva' in nome.lower()))