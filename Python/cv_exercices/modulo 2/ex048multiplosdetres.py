# Faça um programa que calcule a soma entre todos os números impares
# que são multiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma += n
        cont += 1
print(f'A soma dos', (cont), 'valores é igual a', (soma))
    