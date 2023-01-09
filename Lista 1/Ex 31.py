'''Faça um algoritmo que receba o peso de
uma pessoa, calcule e mostre:
a) o novo peso se a pessoa engordar 15% sobre o
peso digitado;
b) o novo peso se a pessoa emagrecer 20% sobre o
peso digitado.'''

p = float(input('Digite seu peso em Kg: '))
a = p + p * 15 / 100
b = p - p * 20 / 100

print('Você atualmente pesa {} Kg\n'
      'se engordar 15% pesará {} Kg\n'
      'se emagrecer 20% pesará {} Kg.'.format(p, a, b))
