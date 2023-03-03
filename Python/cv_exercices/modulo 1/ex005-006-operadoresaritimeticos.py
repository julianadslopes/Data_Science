#Desenvolva um programa que leia um numero na tela
#Mostre seu antecessor, seu sucessor, o dobro, o triplo e sua raiz quadrada

num = int(input('Digite um numero: '))
print(' O antecessor de {} vale {}\n O sucessor de {} vale {}'.format(num, (num-1), num, (num+1)))
print(' O drobro de {} vale {}\n O triplo de {} vale {}\n A raiz quadrada de {} vale {:.2f}'.format(num, (num*2), num, (num*3), num, num**(1/2)))
