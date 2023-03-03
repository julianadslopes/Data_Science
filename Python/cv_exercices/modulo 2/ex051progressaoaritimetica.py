# Faça um programa que leia o primeiro termo de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a Razão da PA: '))
decimo = primeiro_termo + (10 - 1) * razao

for n in range(primeiro_termo, decimo + razao, razao):
    print('{}'.format(n), end=' ')
