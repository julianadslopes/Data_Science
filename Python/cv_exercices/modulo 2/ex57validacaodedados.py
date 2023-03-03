# Faça um programa que leia o sexo de uma pessoa e só aceite se os valores for M ou F.

sexo = str(input('Informe seu sexo: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. informe seu sexo: ')).strip().upper()[0]
print('Sexo {} informado com sucesso.'.format(sexo))
