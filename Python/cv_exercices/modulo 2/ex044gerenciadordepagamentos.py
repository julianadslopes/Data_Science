# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# a vista dinheiro ou cheque: 10% de desconto
# a vista no cartao: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartao: 20% de juros

# mostrando na tela o nome da loja
print('{:=^40}'.format('Lojas Bruno'))

# armazenando o valor do produto na variavel produto
valor_produto = float(input('Digite o valor do produto: R$ '))
print('Seu produto custa R$ {:.2f}.'.format(valor_produto))
print('-=-' * 13)

# mostrando as opçoes de pagamento
print('''Opções de pagamento
[1] - A vista no dinheiro ou cheque
[2] - A vista no cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão''')

# armazenando a forma de pagamento na variavel
opcao_pagamento = int(input('Digite a opção de pagamento: '))
print('-=-' * 13)

# estrutura das condições de pagamento

if opcao_pagamento == 1:
    valor_final = valor_produto - (valor_produto * 0.10)
    print('O valor a vista no dinheiro ou cheque é de R$ {:.2f}.'.format(valor_final))
elif opcao_pagamento == 2:
    valor_final = valor_produto - (valor_produto * 0.05)
    print('O valor a vista no cartão é de R$ {:.2f}.'.format(valor_final))
elif opcao_pagamento == 3:
    valor_final = valor_produto / 2
    print('Você pagará o valor total do produto sem desconto.')
    print('2 parcelas de R$ {:.2f} cada uma.'.format(valor_final))
elif opcao_pagamento == 4:
    parcela = int(input('Em quantas parcelas deseja pagar? ')) # armazenando o numero de parcelas dentro da variável
    if parcela >= 3:
        valor_final = valor_produto + (valor_produto * 0.20)
        valor_final_parcela = valor_final / parcela
        print('Você pagará o produto com um acréscimo de 20% no valor total.')
        print('O valor total do produto ficou em R$ {:.2f}.'.format(valor_final))
        print('{} parcelas de R$ {:.2f} cada uma.'.format(parcela, valor_final_parcela))
    else:
        print('O número de parcelas para esta condição deve ser maior ou igual a 3.')

# mostrando a opção inválida caso o usuário digite numeros diferentes de 1 a 4.
else:
    print('Opção de pagamento inválida. Tente novamente!')
print('-=-' * 13)


