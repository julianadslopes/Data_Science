# Faça um programa que leia um número inteiro e diga se ele é um número primo.

num = int(input('Digite um número: '))

total = 0

for n in range(1, num + 1):
    if num % n == 0:
        total = total + 1
    else:
        print('{}'.format(n), end=' ')
print('\nO número {} foi divisível {} vezes.'.format(num, total))

if total == 2:
    print('\nPor isso ele é PRIMO!')
else:
    print('\nPor isso ele não é Primo.')
