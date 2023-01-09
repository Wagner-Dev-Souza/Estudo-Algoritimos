'''Faça um algoritmo que receba o preço
de um produto, calcule e mostre o novo preço,
sabendo-se que este sofreu um desconto de 10%.'''

p = float(input('Insira o preço do produto: R$ '))
np = p - p * 10 / 100

print('O novo preço é de R$ {:.2f}'.format(np))