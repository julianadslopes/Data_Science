#Escreva um programa que perunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00 calcule um aumento de 10%.
#Para salários inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o salário do funcionário? '))

if salario > 1250.00:
    aumento = salario + (salario * 0.10)
    print('O seu aumento foi de R$ {:.2f}.'.format(aumento))
else:
    aumento = salario + (salario * 0.15)
    print('O seu aumento foi de R$ {:.2f}.'.format(aumento))
