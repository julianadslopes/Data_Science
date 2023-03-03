#Desenvolva um programa que pergunte a distancia da sua viagem em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km.
#E cobrando R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem em km? '))
# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
if distancia <= 200:
    print('Sua viagem custa R$ {:.2f}'.format(distancia * 0.50))
else:
    print('Sua viagem custa R$ {:.2f}'.format(distancia * 0.45))
