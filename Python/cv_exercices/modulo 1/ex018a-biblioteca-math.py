from math import sin, cos, tan, radians
angulo = float(input('Digite um angulo: '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))
print('Analisando o angulo que mede {} graus\n Seno vale {:.2f}\n Cosseno vale {:.2f}\n Tangente vale {:.2f}'
      .format(angulo, sen, cos, tang))