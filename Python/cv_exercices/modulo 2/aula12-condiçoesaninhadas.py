# Condições Aninhadas

""" if (condição):
     bloco1
    elif (condição):
     bloco2
    elif (condição):
     bloco3
    else:
     bloco4
"""

nome = str(input('Qual é o seu nome? '))
if nome == 'Bruno':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Seu nome é bem bonito!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))