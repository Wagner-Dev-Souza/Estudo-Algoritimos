'''Faça um algoritmo que receba o peso de
uma pessoa em quilos, calcule e mostre esse peso
em gramas.'''

pk = float(input('Digite seu peso em Kg: '))
pg = pk * 1000

print('Você pesa {:.0f} gramas'.format(pg))
