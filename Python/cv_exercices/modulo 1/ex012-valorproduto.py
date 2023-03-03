#Faça um programa que leia um valor de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Valor do produto: '))
desconto = produto - (produto * 0.05) # ou produto - ( produto * 5 / 100)
print('Valor do produto com desconto: {:.2f}'.format(desconto))