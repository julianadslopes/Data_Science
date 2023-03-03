# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km prcorridos? '))
totaldias = dias * 60.00
totalkm = km * 0.15
total = totaldias + totalkm  # (dias * 60.00) + (km * 0.15)
print('Total a pagar de aluguel do carro: R$ {:.2f}'.format(totaldias))
print('Total a pagar pelos km percorridos: R$ {}'.format(totalkm))
print('Total a pagar: R$ {}'.format(total))

