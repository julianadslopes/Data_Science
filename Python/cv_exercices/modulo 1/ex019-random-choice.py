# Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele.
# Ler o nome dos alunos e escrever o nome do escolhido

import random
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista_alunos) # choice é usado para escolher um valor dentro da lista
print('O aluno escolhido foi {}'.format(escolhido))
