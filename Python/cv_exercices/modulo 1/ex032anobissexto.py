#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.
from datetime import date
ano = int(input('Digite um ano para ser analisado ou 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # pega o ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))