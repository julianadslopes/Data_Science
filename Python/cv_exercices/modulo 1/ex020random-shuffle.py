# O professor quer sortear a ordem da apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada.

import random

aluno1 = input('Digite  nome do primeiro aluno(a): ')
aluno2 = input('Digite o nome do segundo aluno(a): ')
aluno3 = input('Digite o nume do terceiro aluno(a): ')
aluno4 = input('Digite o nome do quarto aluno(a): ')
lista_aluno = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista_aluno)

print('A ordem da apresentação será: {}'.format(lista_aluno))
