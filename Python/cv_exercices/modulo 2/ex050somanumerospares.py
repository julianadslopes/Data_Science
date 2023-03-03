# Desenvolva um programa que leia 6 numeros inteiros.
# Mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere.

soma = 0
cont = 0

for n in range(1, 7):
    num = int(input('Digite o {} valor: '.format(n)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('A soma dos {} números pares é igual a {}'.format(cont, soma))
