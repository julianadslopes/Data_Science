#Desenvolva um programa que leia as duas notas de uma aluno, calcule e mostre a sua média.

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2)/2
print(' Sua primeira nota é: {:.1f}\n Sua segunda nota é: {:.1f}\n Sua média é: {:.1f}'
      .format(nota1, nota2, media))