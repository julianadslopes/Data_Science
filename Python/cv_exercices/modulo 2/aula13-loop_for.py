for count in range(0, 6):
    print(count)
print('FIM')

for count in range(6, 0, -1):
    print(count)
print('fim')

for count in range(0, 7, 2):
    print(count)


numero = int(input('Digite um número: '))
for count in range(0, numero + 1):
    print(count)

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for count in range(inicio, fim + 1, passo):
    print(count)
print('FIM')

for count in range(0, 3):
    nome = input('Digite um nome: ')
    print(count)

soma = 0
for count in range(0, 4):
    numero = int(input('Digite um numero: '))
    soma += numero
print('A soma dos números vale {}'.format(soma))
