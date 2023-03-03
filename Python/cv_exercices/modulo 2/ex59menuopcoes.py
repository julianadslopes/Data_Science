#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

opcao = 0
while opcao != 5:
    print('''   [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos números
    [5] - sair do programa''')
    opcao = int(input('Qual a sua opção? '))

    if opcao == 1:
        resultado = valor1 + valor2
        print('O resultado de {} + {} é igual a {}.'.format(valor1, valor2, resultado))
    elif opcao == 2:
        resultado = valor1 * valor2
        print('O resultado de {} x {} é igual a {}.'.format(valor1, valor2, resultado))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print('O maior valor entre {} e {} é {}.'.format(valor1, valor2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
print('Fim do programa!')


