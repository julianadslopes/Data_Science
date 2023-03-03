# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar no serviço militar
# Se é hora de se alistar
# Seu programa também deverá mostrar o tempo que falta ou se passou do prazo.

from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano_atual))

if idade == 18:
    print('É hora de se alistar no exército!')
elif idade < 18:
    anos_restantes = 18 - idade
    print('Ainda falta(m) {} ano(s) para o seu alistamento.'.format(anos_restantes))
    ano_alistamento = ano_atual + anos_restantes
    print('Seu alistamento será em {} ano(s).'.format(ano_alistamento))
elif idade > 18:
    anos_restantes = idade - 18
    print('Você deveria ter se alistado há {} ano(s).'.format(anos_restantes))
    ano_alistamento = ano_atual - anos_restantes
    print('Seu alistamento foi em {}.'.format(ano_alistamento))



