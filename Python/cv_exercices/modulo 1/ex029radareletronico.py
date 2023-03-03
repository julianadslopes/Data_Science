#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade do carro em km/h: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print('Você foi multado!')
    print('O valor da multa será de R$: {:.2f}'.format(multa))
print('Você está na velocidade permitida.')