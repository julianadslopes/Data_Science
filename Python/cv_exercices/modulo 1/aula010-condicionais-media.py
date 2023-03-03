nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7:
    print('Parabéns, sua média é {:.1f}. Você foi aprovado!'.format(media))
else:
    print('Estude mais, sua média é {:.1f}. Você está reprovado.'.format(media))