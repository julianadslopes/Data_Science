# A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta.
# Mostre a sua categoria de acordo com a idade:
# Até 9 anos: Mirim, Até 14 anos: Infantil, Até 19 anos: Junior, Até 20 anos: Senior, Acima: Master

from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
categoria = ano_atual - ano_nascimento

if categoria <= 9:
    print('Você tem {} ano(s). Sua categoria é Mirim.'.format(categoria))
elif categoria > 9 and categoria <= 14:
    print('Você tem {} ano(s). Sua categoria é Infantil.'.format(categoria))
elif categoria > 14 and categoria <= 19:
    print('Você tem {} ano(s). Sua categoria é Junior.'.format(categoria))
elif categoria == 20:
    print('Você tem {} ano(s). Sua categoria é Senior.'.format(categoria))
else:
    print('Você tem {} ano(s). Sua categoria é Master.'.format(categoria))