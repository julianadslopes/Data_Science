# Faça um programa que mostre na tela uma contagem regressiva para queima de fogos.
# Indo de 10 até 0 com uma pausa de 1 segundo entre eles.

from time import sleep

for cont in range(10, -1, -1):
    sleep(1)
    print(cont)
print("FOGOS!")
    