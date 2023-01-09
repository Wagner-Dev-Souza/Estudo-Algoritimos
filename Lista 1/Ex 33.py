'''Faça um algoritmo que calcule e
mostre a área de um trapézio. Sabe-se que:
A = (base maior + base menor)* altura)/2 ;'''

print('Informe as medidas em metros')
B = float(input('Informe a base maior do trapézio: '))
b = float(input('Informe a base menor do trapézio: '))
h = float(input('Informe a altura do trapézio: '))
a = ((B + b) * h) / 2

print('A área do trapézio é {} m²'.format(a))
