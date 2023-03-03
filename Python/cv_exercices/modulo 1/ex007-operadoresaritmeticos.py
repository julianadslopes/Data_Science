n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
som = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
divi = n1 // n2
exp = n1 ** n2
print('A soma vale {}, a subtraçao vale {}, a multiplicaçao vale {}'.format(som, sub, mult), end=' ') # end não quebra linha
print('A divisao vale {:.3f},\n a divisao inteira vale {},\n a exponenciaçao vale {}'.format(div, divi, exp)) # \n quebra a linha