'''Faça um algoritmo que calcule e mostre
a área de um losango. Sabe-se que: A =
(diagonal_maior * diagonal_menor)/2;'''

print('Informe as medidas em metros')
D = float(input('Informe a diagonal maior do losango: '))
d = float(input('Informe a diagonal menor do losango: '))
a = (D * d) / 2

print('A área do losango é {} m²'.format(a))