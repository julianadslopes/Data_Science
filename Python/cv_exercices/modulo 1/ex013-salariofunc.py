#Faça um programa que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

salario = float(input('Salário do funcionário: R$ '))
aumento = salario + (salario * 15 / 100)
print('Novo salário com aumento: R$ {}'.format(aumento))