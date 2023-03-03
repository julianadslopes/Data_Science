# Escreva um programa para aprovar um empréstimo bancário para compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário, ou então o impréstimo será negado.

valor_casa = float(input('Digite o valor da casa: R$ '))
salario_comprador = float(input('Digite o salário do comprador: R$ '))
anos_pagamento = int(input('Em quantos anos deseja pagar a casa? '))
salario_aprovacao = salario_comprador * 30 / 100
prestacao = valor_casa / (anos_pagamento * 12)

print('Para pagar uma casa de R$ {:.2f} em {} anos,'.format(valor_casa, anos_pagamento), end='')
print(' a prestação será de R$ {:.2f}.'.format(prestacao))

if prestacao <= salario_aprovacao:
    print('Empréstimo pode ser aprovado!')
else:
    print('Empréstimo negado!')


