#Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))
numero3 = int(input('Digite o terceiro valor: '))
#verificando o menor número
if numero1 < numero2 and numero1 < numero3:
    menor = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor= numero3
#verificando o maior número
if numero1 > numero2 and numero1 > numero3:
    maior = numero1
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print('O menor número digitado foi {}.'.format(menor))
print('O maior número digitado foi {}.'.format(maior))

