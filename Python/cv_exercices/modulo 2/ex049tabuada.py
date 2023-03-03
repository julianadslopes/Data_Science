# Mostre a tabuada de um número que o usuário escolher usando laço for.

# tabuada = int(input('Qual a tabuada do número: '))

#for n in range(1, 11):
#    multiplicacao = n * tabuada
#    print(multiplicacao)

num = int(input('Digite um número para saber a sua tabuada: '))

for n in range(1, 11):
    print((num), 'x', (n), '=', (num * n))