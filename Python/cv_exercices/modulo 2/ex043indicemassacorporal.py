# Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
# Calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print('Você está abaixo do peso. Seu IMC é {:.2f}.'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Você está no peso ideal! Seu IMC é {:.2f}.'.format(imc))
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso. Seu IMC é {:.2f}.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Você está obeso. Seu IMC é {:.2f}.'.format(imc))
else:
    print('Você está mórbido. Seu IMC é {:.2f}.'.format(imc))